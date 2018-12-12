from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Language

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None,
            {'fields': ('username', 'password')}
        ),
        
        ('Personal info',
            {'fields': ('first_name', 'last_name', 'email')}
        ),

        ('Language info',
            {'fields': ('learning_languages', 'fluent_languages')}
        ),

        ('Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser',
                        'groups', 'user_permissions')}
        ),
        
        ('Important dates',
            {'fields': ('last_login', 'date_joined')}
        )
    )
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Language)