# Generated by Django 2.2.5 on 2019-10-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20191009_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
