# Generated by Django 4.0.3 on 2022-03-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FizzBuzz',
            fields=[
                ('fizzbuzz_id', models.AutoField(primary_key=True, serialize=False)),
                ('useragent', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
