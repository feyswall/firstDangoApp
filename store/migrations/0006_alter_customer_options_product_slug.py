# Generated by Django 4.0.6 on 2022-07-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_collection_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
