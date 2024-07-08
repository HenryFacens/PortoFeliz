from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Sector, Interaction, Feedback, AdminUser

admin.site.site_header = "Cidadania Transparente"
admin.site.site_title = "Cidadania Transparente"
admin.site.index_title = "Bem-vindo ao Portal de Cidadania Transparência"

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'join_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lgn', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'like_dislike', 'created_at', 'updated_at')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'sector', 'interaction', 'created_at', 'updated_at')
    search_fields = ('full_name', 'phone')

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'active', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'user__username')
