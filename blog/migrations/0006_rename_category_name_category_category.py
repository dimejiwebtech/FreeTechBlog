# Generated by Django 5.1.4 on 2024-12-17 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='category',
        ),
    ]
