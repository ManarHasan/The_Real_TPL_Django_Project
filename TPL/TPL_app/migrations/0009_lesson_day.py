# Generated by Django 2.2.4 on 2020-12-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPL_app', '0008_auto_20201225_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='day',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
