# from django.db import models

# from .ProductModel import ProductModel
# from .NamedModel import NamedModel
# from users.models.Users import Users,UserAddressModel
# # from users.models.Address import UsersAddressModel
# from .ProductModel import MeasuringModel

# ORDERED_STATUS_VALUE=[
#     ('OD', 'Order Delivered'),
#     ('OW', 'On The Way'),
#     ('PP', 'Packaging Process Is Going On'),
#     ('OS', 'Out For Shipping'),
#     ('NA', 'Not Avaliable Service right now')
# ]

# class OrderMeasureModel(NamedModel):
#     ordered_prod = models.OneToOneField(ProductModel,on_delete=models.CASCADE)
#     measure_params = models.OneToOneField(MeasuringModel,on_delete=models.CASCADE)
#     class Meta:
#         abstract = False

# class UserOrder(NamedModel):
# # An user can have multiple order.
#     user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=False,related_name="user_related_to_order")
# # An order will be associaeted to single user address
#     address = models.OneToOneField(UserAddressModel,on_delete=models.CASCADE,blank=False)
# # measurement of ordered items with product ordered.
#     ordered_prod = models.ManyToManyField(OrderMeasureModel,blank=False)
# # ordered status 
#     order_status = models.CharField(max_length=2,choices=ORDERED_STATUS_VALUE,default='OW')
# # shipping method for delivery
# # payment method for ordering

#     def __str__(self) -> str:
#         return self.name

#     class Meta : 
#         abstract = False
#         ordering=['created_at']

