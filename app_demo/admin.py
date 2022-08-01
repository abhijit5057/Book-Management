from unicodedata import name
from urllib import request
from django.contrib import admin
# Register your models here.
from import_export import resources
from app_demo.models import Book,Author,Category
from import_export.admin import ImportExportActionModelAdmin
from import_export import fields
from .models import Book
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget,ManyToManyWidget
from django.contrib.contenttypes.models import ContentType
class BookResource(resources.ModelResource):
    author = fields.Field(
        column_name='author',
        attribute='author',
        widget=ForeignKeyWidget(Author, 'name'))
    categories = fields.Field(
        column_name='categories',
        attribute='categories',
        widget=ManyToManyWidget(Category,field='name', separator='|'))
    
    class Meta:
        model=Book
        fields = ('id','name', 'author','imported','published','price','categories')
        export_order = ('id','name' ,'price', 'author','published','categories')
        exclude = ('imported', )


class BookAdmin(ImportExportModelAdmin):
    exclude=[ 'date_joined', 'email', 'first_name', 'groups',  'is_active', 'is_staff', 'is_superuser', 'last_login', 'last_name', 'logentry', 'password', 'user_permissions', 'username']
admin.site.register(Book, BookAdmin)






class AuthorModelAdmin(admin.ModelAdmin):
    def _allow_edit(self, obj=None):
        if not obj:
            return True
        return not (obj.is_staff or obj.is_superuser)

    def has_change_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_delete_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True
    
    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (obj and obj.id == request.user.id)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        return qs if user.is_superuser else qs.filter(id=user.id)
   
            
class AuthorResource(resources.ModelResource):
    class Meta:
        model=Author

class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
admin.site.register(Author,AuthorModelAdmin)



admin.site.register(Category)


