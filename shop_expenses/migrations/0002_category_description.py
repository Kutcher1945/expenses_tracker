# Generated by Django 4.1.5 on 2023-06-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
