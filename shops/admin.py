from django.contrib import admin 

from .models.ProductModel import *
from .models.NamedModel import *
from .models.ShopModel import *
from .models.CartModel import CartModel
from .models.TagModel import Tagmodel


# Register your models here.

# admin.site.register(ProductCountableModel)
# admin.site.register(ProductMeasurableModel)

# admin.site.register(PouchModel)



# admin.site.register(Tagmodel)

# # changing the editbale tag field in product 
# # adding the product tag to the init list 
# class TagInline(admin.StackedInline):
#     model = ProductModel.tags.through
#     extra = 1

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','measuring_choices',)
#     inlines = (TagInline,) 
 
# admin.site.register(ProductModel,ProductAdmin)


# # changing the admin pannel field for shops

# class ShopProductInline(admin.StackedInline):
#     model = ShopModel.shop_prouducts.through
#     extra = 1
#     verbose_name = "Add Products From Dropdown According to Shops"
# class ShopPartnersInline(admin.StackedInline):
#     model = ShopModel.partners.through
#     extra = 1
#     verbose_name = "Add Shop Prtner From Dropdown According to Shops"
# class ShopShopAddressInline(admin.StackedInline):
#     model = ShopModel.shop_address.through
#     extra = 1
#     verbose_name = "Add Ahop Address From Dropdown According to Shops"

# class ShopAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     inlines = (ShopProductInline,ShopPartnersInline,ShopShopAddressInline)

# admin.site.register(ShopModel,ShopAdmin)

# # Edit m2m field in cartmodel admin pannel

# class CartProductInline(admin.StackedInline):
#     model = CartModel.cart_product.through
#     extra = 1
#     verbose_name = "Add Product to the cart for any users "

# class CartAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     inlines = (CartProductInline, )

# admin.site.register(CartModel,CartAdmin) 


# # Edit m2m field in Users Order Admin Pannel

# # class UserOrderOrderedProdInline(admin.StackedInline):
# #     model = UserOrder.ordered_prod.through
# #     extra = 1
# #     verbose_name = "Modify User Ordered Product"

# # class UserOrderAdmin(admin.ModelAdmin):
# #     list_display = ('name',)
# #     inlines = (UserOrderOrderedProdInline,)

# # admin.site.register(UserOrder,UserOrderAdmin)


# # Edit Measure Model m2m field in admin pannel


# # class MeasuringModelCountableInline(admin.StackedInline):
# #     model = MeasuringModel.countable_product.through
# #     extra = 1
# #     verbose_name = "Add countable product"

# # class MeasuringModelMeasurableInline(admin.StackedInline):
# #     model = MeasuringModel.measurable_product.through
# #     extra = 1
# #     verbose_name = "Add measuring product "

# # class MeasuringmodelAdmin(admin.ModelAdmin):
# #     inlines = (MeasuringModelCountableInline,MeasuringModelMeasurableInline,)

# # admin.site.register(MeasuringModel,MeasuringmodelAdmin)



