# Generated by Django 3.2 on 2022-03-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20211229_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='flat',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=60),
        ),
    ]