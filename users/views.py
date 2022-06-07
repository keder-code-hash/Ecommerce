from webbrowser import get
from rest_framework.views import APIView
from rest_framework.response import Response 
# from users.permissions import IsOwnerOrReadOnly

from .utils_serializers import LoginSerializer,LogoutSerializer,ResetPasswordEmailSentSerializers,ResetPasswordSerializers
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from django.urls import reverse_lazy
from django.template.loader import get_template
from django.core.mail import EmailMessage

from django.utils.http import urlsafe_base64_decode
from django.core.exceptions import ValidationError

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from rest_framework.viewsets import mixins,GenericViewSet
from .models.Users import Users
from .serializers.Users import UsersSerializers

# from .CustomJwtAuth import MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import get_authorization_header

from .CustomJwtAuth import CustomJwtAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model

# permission class is set to authinticate or read only
# persmission
class UserView(APIView): 
    authentication_classes = [CustomJwtAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        users=Users.objects.all()
        auth_header = get_authorization_header(request)
        # print(get_user_model())
        return Response(UsersSerializers(users,many=True).data,status=status.HTTP_200_OK) 



############## Register View ##############################

class CustomModelViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        GenericViewSet):
    pass

    

class RegisterView(CustomModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


# ############## LogIn & LogOut View ##############################

class LogInView(APIView):
    serializer_class = LoginSerializer

    def post(self,request): 
        
        serializers_data = self.serializer_class(data=request.data)
        serializers_data.is_valid(raise_exception=True)
        # print(serializers_data.validated_data)
 
        return Response(serializers_data.data,status=status.HTTP_200_OK)

class LogOutView(APIView):
    serializer_class = LogoutSerializer
    def post(self,request,format=None):
        serializers_data = self.serializer_class(data=request.data)
        serializers_data.is_valid(raise_exception=True)
        try : 
            token = RefreshToken(serializers_data.data)
            token.blacklist()
        except TokenError:
            msg = 'Successfully logged out'
        return Response(msg,status=status.HTTP_200_OK)

# ########## Password Reset #############

def send_mail(subject_template_name, email_template_name,
                  context, from_email, to_email, message ,html_email_template_name=None):
         
        mail = EmailMessage(
                subject="Reset Password",
                body=message,
                from_email="kedernath.mallick.tint022@gmail.com",
                to=["kedernath.mallick.tint022@gmail.com"],
                reply_to=["kedernath.mallick.tint022@gmail.com"],
            )
        mail.content_subtype = "html"
        mail.send() 

# # just send the password reset email from django
# # contains the link 
class SendResetPassEmail(APIView):
    serializer_class = ResetPasswordEmailSentSerializers
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')

        if Users.objects.filter(email__iexact=email).exists():
            user = Users.objects.get(email__iexact = email)

            # uidb64 = user id encoded in base 64
            # "reset/<uidb64>/<token>/"

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token  = PasswordResetTokenGenerator().make_token(user=user)
            
            # 127.0.0.1:8000
            curr_site = get_current_site(request=request).domain
            site_name = get_current_site(request=request).name

            url = reverse_lazy("password_reset_confirm",kwargs={
                "uidb64" : uidb64,
                "token" :token
            })

            final_password_reset_link = curr_site+str(url)

            subject_template_name = "email/password_reset_subject.txt"
            email_template_name = None
            from_email = "kedernath.mallick.tint022@gmail.com"
            to_email = email
            html_email_template_name="email/reset_pass.html"


            context = {
                    "resetPass_url" : final_password_reset_link
                }
            message = get_template("email/reset_pass.html").render(context)

            send_mail(subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name , message )


        return Response({"final_link" : final_password_reset_link},status=status.HTTP_200_OK)

class ResetPassTODB(APIView):
    serializer_class = ResetPasswordSerializers

    def get_user(self, uidb64):
        try: 
            uid = urlsafe_base64_decode(uidb64).decode()
            user = Users._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            Users.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user
    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)

        uidb64 = kwargs.get("uidb64")
        token = kwargs.get("token")

        user = self.get_user(uidb64)
        serializer.save(user)
        
        return Response(UsersSerializers(self.get_user(uidb64)).data, status = status.HTTP_200_OK)

# #############################################################


# # whenever send a request from frontend to backend use ACCESS TOKEN , refresh can't be verified in backend
# # when a user data is required in front end then use REFRESH TOKEN


# # login - api/token/(return 401 or wrong creds)
# # logout - 
#     # - add user refresh token to the blacklist api -(http://127.0.0.1:8000/api/token/blacklist/).
#     # - now after logging out if a user has the previous refresh token , he cant be able to hit any API cause it require a access token.
#     # - If an access token is being expier we have to generate the access token with the refresh toke.But the refresh token is blacklisted.
#     # - Any API can be accessed further untill user again logged in.
# # reset_password - password_reset/
# # update_user - register/(put)
# # activate_user - 