# Generated by Django 4.2 on 2023-06-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_department_dep_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dep_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='department',
            name='dep_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]