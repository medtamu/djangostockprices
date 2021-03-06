# Generated by Django 2.0.5 on 2018-08-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=6)),
                ('Date', models.DateTimeField()),
                ('Open', models.FloatField()),
                ('High', models.FloatField()),
                ('Low', models.FloatField()),
                ('Close', models.FloatField()),
                ('Volume', models.IntegerField()),
                ('Adjclose', models.FloatField()),
            ],
        ),
    ]
