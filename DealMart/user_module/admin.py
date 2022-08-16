from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User

class UserAdminConfig(UserAdmin):
    search_fields = ('email','first_name','last_name') 
    ordering = ('email',)
    list_display = ('email','first_name','last_name')

    fieldsets = (
        (None,{'fields':('email','first_name','last_name',)}),
        ('Permissions',{'fields':('is_staff','is_active')}),
        ('Personal',{'fields':('phone','address','profile_pic')})
    )   
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2',)
        }),
    )

admin.site.register(User,UserAdminConfig)