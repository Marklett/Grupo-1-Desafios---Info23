# Generated by Django 4.2.2 on 2023-07-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0014_remove_users_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id_user',
        ),
        migrations.AddField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='registration_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
