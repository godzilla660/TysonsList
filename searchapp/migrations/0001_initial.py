# Generated by Django 3.1.4 on 2023-12-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=260)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
