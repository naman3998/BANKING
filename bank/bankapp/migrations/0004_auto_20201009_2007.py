# Generated by Django 3.1.1 on 2020-10-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_auto_20201009_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
    ]
