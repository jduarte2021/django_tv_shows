# Generated by Django 3.2.5 on 2021-08-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_show_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
