# Generated by Django 4.2.2 on 2023-07-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0008_rename_user_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
