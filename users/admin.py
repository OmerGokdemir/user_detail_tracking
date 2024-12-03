from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Address, Company, Geo

admin.site.register(Geo)
admin.site.register(Address)
admin.site.register(Company)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Kullanıcı yönetimi alanları
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'website', 'address', 'company')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    # Yeni kullanıcı eklerken görünecek alanlar
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    # Admin panelinde görünen alanlar
    list_display = ('email', 'username', 'name', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'name')
    ordering = ('email',)

    # Kullanıcıyı kaydederken kimlik doğrulaması
    filter_horizontal = ('groups', 'user_permissions')

    # Admin sayfasındaki "address" ve "company" için ilgili nesneleri görüntülemek için
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')



