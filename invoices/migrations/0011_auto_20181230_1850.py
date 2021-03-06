# Generated by Django 2.1.4 on 2018-12-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("invoices", "0010_auto_20181230_1657")]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="invoice_amount",
            field=models.CharField(
                default="22.00", max_length=10, verbose_name="Invoice amount"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="invoice",
            name="invoice_tax_amount",
            field=models.CharField(
                default="0.00", max_length=10, verbose_name="Invoice tax"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="invoice",
            name="invoice_tax_rate",
            field=models.CharField(
                default="0.00", max_length=5, verbose_name="Invoice tax rate"
            ),
            preserve_default=False,
        ),
    ]
