# Generated by Django 2.2.5 on 2019-09-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190923_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='newborn_tpn',
            name='aminoasit',
            field=models.IntegerField(default=1, verbose_name='Aminoasit (gr)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newborn_tpn',
            name='glukoz',
            field=models.IntegerField(default=6, verbose_name='Glukoz (gr)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newborn_tpn',
            name='kalsiyum',
            field=models.IntegerField(default=500, verbose_name='Calsiyum (meq)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newborn_tpn',
            name='potasyum',
            field=models.IntegerField(default=1, verbose_name='Potasyum (meq)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newborn_tpn',
            name='sodyum',
            field=models.IntegerField(default=1, verbose_name='Sodyum (meq)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newborn_tpn',
            name='total',
            field=models.IntegerField(default=60, verbose_name='Total  cc/kg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newborn_tpn',
            name='hafta',
            field=models.FloatField(verbose_name='Hafta (gh)'),
        ),
        migrations.AlterField(
            model_name='newborn_tpn',
            name='kilo',
            field=models.FloatField(verbose_name='Kilo (kg)'),
        ),
    ]