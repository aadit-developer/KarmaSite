# Generated by Django 3.0.7 on 2020-06-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='')),
                ('product_price', models.IntegerField()),
                ('product_stock', models.IntegerField()),
            ],
        ),
    ]
