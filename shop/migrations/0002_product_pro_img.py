# Generated by Django 3.0.8 on 2020-09-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_img',
            field=models.ImageField(default='', upload_to='shop/image'),
            preserve_default=False,
        ),
    ]
