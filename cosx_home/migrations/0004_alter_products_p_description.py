# Generated by Django 4.1.2 on 2022-11-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cosx_home", "0003_products_p_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="p_description",
            field=models.CharField(max_length=500),
        ),
    ]