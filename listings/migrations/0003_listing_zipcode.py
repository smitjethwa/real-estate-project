# Generated by Django 4.1 on 2022-09-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_realtor_id_listing_realtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
