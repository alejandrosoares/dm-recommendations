# Generated by Django 4.2.6 on 2023-10-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
