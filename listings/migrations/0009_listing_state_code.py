# Generated by Django 4.1 on 2022-09-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_rename_zipcode_listing_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state_code',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
