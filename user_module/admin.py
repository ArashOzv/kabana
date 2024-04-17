from django.contrib import admin

from user_module.models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_editable = ('is_active', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)