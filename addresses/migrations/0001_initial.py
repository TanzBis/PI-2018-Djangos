# Generated by Django 3.2 on 2022-03-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=30)),
                ('house', models.CharField(blank=True, max_length=10, null=True)),
                ('flat', models.IntegerField(blank=True, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
    ]
