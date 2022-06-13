from django.contrib import admin

from .models.Users import Users,UserAddressModel

 
admin.site.register(UserAddressModel)

# edit user model admin panel

class UserAdressInline(admin.StackedInline):
    model = Users.address.through
    extra = 1
    verbose_name = "Add address to this user"

class UserDeliveryAdressInline(admin.StackedInline):
    model = Users.delivery_address.through
    extra = 1
    verbose_name = "Add delivery address to this user"
    
class CustomAdminPanel(admin.ModelAdmin):
    inlines = (UserAdressInline,UserDeliveryAdressInline,)
    list_display = ('username','email',) 

admin.site.register(Users,CustomAdminPanel)