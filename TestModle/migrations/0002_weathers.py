# Generated by Django 2.2 on 2019-04-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='weathers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Weather', models.CharField(max_length=80)),
                ('Teap', models.CharField(max_length=40)),
            ],
        ),
    ]
