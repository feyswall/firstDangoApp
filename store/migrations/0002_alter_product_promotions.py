# Generated by Django 4.0.1 on 2022-04-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(related_name='product', to='store.Promotion'),
        ),
    ]
