from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from .forms.TagForm import TagChangeListForm
from django.forms import BaseModelFormSet

from .models.ProductModel import *
from .models.NamedModel import *
from .models.PouchModel import *
from .models.ShopModel import *
from .models.UserOrders import UserOrder,OrderMeasureModel
from .models.CartModel import CartModel
from .models.TagModel import Tagmodel


# Register your models here.

# admin.site.register(MeasuringModel)
# admin.site.register(ProductCountableModel)
# admin.site.register(ProductMeasurableModel)

# admin.site.register(PouchModel)

# admin.site.register(ShopModel)

# admin.site.register(CartModel)
# admin.site.register(UserOrder)
# admin.site.register(OrderMeasureModel)


admin.site.register(Tagmodel)

# changing the editbale tag field in product

class MyAdminFormSet(BaseModelFormSet):
    queryset = Tagmodel.objects.all()


class ProductTagchangeList(ChangeList):
    def __init__(self, request, model , list_display, list_display_links, list_filter , date_hierarchy , search_fields , list_select_related, list_per_page, list_max_show_all, list_editable, model_admin, sortable_by) :
        super(ProductTagchangeList,self).__init__(request, model, list_display, list_display_links, list_filter, date_hierarchy, search_fields, list_select_related, list_per_page, list_max_show_all, list_editable, model_admin, sortable_by)

        # self.list_display = ['product_images','measuring_choices','tags']
        self.list_editable = ['tags']

class TagInline(admin.TabularInline):
    model = ProductModel.tags.through

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','measuring_choices',)
    inlines = (TagInline,)
    def get_changelist(self, request , **kwargs ) :
        return ProductTagchangeList
    
    def get_changelist_form(self, request, **kwargs):
        return TagChangeListForm
    
    def get_changelist_formset(self, request, **kwargs):
        kwargs['formset'] = MyAdminFormSet
        return super().get_changelist_formset(request, **kwargs)



admin.site.register(ProductModel,ProductAdmin)
