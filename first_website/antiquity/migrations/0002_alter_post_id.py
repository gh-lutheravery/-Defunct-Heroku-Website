# Generated by Django 3.2 on 2021-12-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiquity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
