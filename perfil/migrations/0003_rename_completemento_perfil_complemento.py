# Generated by Django 5.1 on 2024-09-17 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_endereco_alter_perfil_numero_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='completemento',
            new_name='complemento',
        ),
    ]
