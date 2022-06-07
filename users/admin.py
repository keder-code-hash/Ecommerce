from django.contrib import admin

from .models.Users import Users,UserAddressModel

# from .models.Address import UsersAddressModel

admin.site.register(Users)
admin.site.register(UserAddressModel)

# admin.site.register(UsersAddressModel)

class CustomAdminPanel(admin.ModelAdmin):
    def __init__(self, model, admin_site ) -> None:
        super().__init__(Users, admin_site)

