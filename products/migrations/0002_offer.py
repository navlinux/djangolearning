# Generated by Django 4.0.4 on 2022-05-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('desc', models.CharField(max_length=1000)),
                ('disc', models.FloatField()),
            ],
        ),
    ]