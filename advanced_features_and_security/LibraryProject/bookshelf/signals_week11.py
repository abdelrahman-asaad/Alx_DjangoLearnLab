# bookshelf/permissions_setup.py

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from book_store.models import Book

def create_groups_and_assign_permissions():
    content_type = ContentType.objects.get_for_model(Book) 

    permissions = {  #built in property to assign permissions
        'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
        'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
        'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
        'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
    }

    groups = {  #built in property to create groups
        'Viewers': ['can_view'],
        'Editors': ['can_view', 'can_create', 'can_edit'],
        'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)  #fetch groub from database or create one
        group.permissions.set([permissions[p] for p in perms]) #ex : permissions[0] for 0 in perms
        group.save()
