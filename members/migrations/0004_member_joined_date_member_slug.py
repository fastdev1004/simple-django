# Generated by Django 4.2 on 2023-05-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_firstname_member_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
