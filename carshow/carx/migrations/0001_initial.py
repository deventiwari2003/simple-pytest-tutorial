# Generated by Django 4.2.5 on 2023-10-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('mileage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('avg_speed', models.IntegerField()),
                ('date_posted', models.DateField()),
            ],
        ),
    ]
