# Generated by Django 3.1.7 on 2021-03-11 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('num', models.CharField(max_length=10)),
                ('town', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('all_adress', models.TextField(max_length=1000)),
                ('phone', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=250)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='products.product')),
            ],
        ),
    ]
