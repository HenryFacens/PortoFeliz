from django.contrib.auth.models import Group, Permission
from django.db import migrations

def create_groups(apps, schema_editor):
    group_names = ['Owner', 'Admin', 'Viewer']
    for name in group_names:
        group, created = Group.objects.get_or_create(name=name)
        
        if name == 'Viewer':
            permissions = Permission.objects.filter(codename__in=['view'])
        elif name == 'Admin':
            permissions = Permission.objects.filter(codename__in=['add', 'change', 'delete'])
        elif name == 'Owner':
            permissions = Permission.objects.all()
        
        for permission in permissions:
            group.permissions.add(permission)

class Migration(migrations.Migration):
    dependencies = [
        ('your_app', 'previous_migration_file'),  # substitua pelo nome do arquivo de migração anterior
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
