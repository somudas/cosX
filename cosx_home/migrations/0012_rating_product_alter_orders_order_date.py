# Generated by Django 4.1.2 on 2022-11-15 05:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cosx_home", "0011_alter_orders_order_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="cosx_home.products",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orders",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 15, 0, 2, 31, 257407, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
