# Generated by Django 3.2 on 2022-03-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='first_name last_name'),
        ),
    ]