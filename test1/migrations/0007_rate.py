# Generated by Django 4.2.3 on 2023-07-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0006_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
    ]
