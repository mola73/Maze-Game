# Generated by Django 5.1.6 on 2025-03-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('moves', models.IntegerField()),
                ('time_elapsed', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
