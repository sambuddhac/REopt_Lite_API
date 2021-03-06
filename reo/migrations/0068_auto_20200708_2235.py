# Generated by Django 2.2.10 on 2020-07-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0067_electrictariffmodel_year_one_to_load_series_bau_kw'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialmodel',
            name='simple_payback_years',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='lcoe_us_dollars_per_kwh',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='storagemodel',
            name='total_rebate_us_dollars_per_kwh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='lcoe_us_dollars_per_kwh',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
