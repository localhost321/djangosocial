# Generated by Django 3.2.9 on 2021-12-06 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211206_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
