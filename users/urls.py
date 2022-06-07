from django.urls import path
from .views import ResetPassTODB,RegisterView,LogInView,LogOutView,SendResetPassEmail,UserView
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views

from rest_framework_simplejwt.views import ( 
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from django.contrib.auth import views
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'API/register',RegisterView ,basename="register")


urlpatterns=[
    path("",UserView.as_view(),name="users"),

    # api for users activity
    path('API/login/',
        LogInView.as_view(),
        name = "login"
    ),
    path('API/logout/',
        LogOutView.as_view(),
        name="logout"
    ),
    path('',include(router.urls)),

    path('API/token/refresh/',
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),

    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),

    # password reset
    path("API/password_reset/", 
        SendResetPassEmail.as_view(), 
        name="password_reset"),
    path(
        "API/reset/<uidb64>/<token>/",
        ResetPassTODB.as_view(),
        name="password_reset_confirm",
    ),

    

    # # path('api-token-auth/', views.obtain_auth_token),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # # path('api/token/refresh/',
    # #     TokenRefreshView.as_view(), 
    # #     name='token_refresh'
    # # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
    #  path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
