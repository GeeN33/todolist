from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login','date_joined')
    fieldsets = (
        (None,
         {'fields':('username', 'password')}),

        ('Personal Info',
         {'fields': ('first_name', 'last_name', 'email')}),

        ('Permission',
         {'fields': ('is_active', 'is_staff', 'is_superuser')}),

        ('Important dates',
         {'fields': ('last_login', 'date_joined')})

    )





# admin.site.register(User,UserAdmin)

