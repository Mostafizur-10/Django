# Generated by Django 4.0.2 on 2022-04-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0007_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AlterField(
            model_name='plot',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
