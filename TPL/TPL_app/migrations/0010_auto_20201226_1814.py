# Generated by Django 2.2.4 on 2020-12-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPL_app', '0009_lesson_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
