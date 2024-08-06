from django.contrib import admin
from employee_register.model import Employee, Position, Product, NewUser

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(NewUser)

class ProductMixIn:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_view_permission(self, request, obj=None):
        return True

@admin.register(Product)
class ProductAdmin(ProductMixIn, admin.ModelAdmin):
    list_display = ("name",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['name'].disabled = True
        
        return form
