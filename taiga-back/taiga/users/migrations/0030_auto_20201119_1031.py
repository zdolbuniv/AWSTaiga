# Generated by Django 2.2.17 on 2020-11-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_user_verified_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]