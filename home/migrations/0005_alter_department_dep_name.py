# Generated by Django 4.2 on 2023-06-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_department_dep_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]