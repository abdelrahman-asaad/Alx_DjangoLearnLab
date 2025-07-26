from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

#____week11____
from django.contrib.auth.admin import UserAdmin #the default used class to represent 'user' in admin and manage users and their permissions
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff'] #the columns appearing in users list in admin interface
    fieldsets = UserAdmin.fieldsets + (         #fieldsets is an attritbtute that controls appears when modifying
        ('معلومات إضافية', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( #add_field is an attritbtute that controls appears when adding new user
        ('معلومات إضافية', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
