# Generated by Django 3.1.1 on 2020-09-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, default='', max_length=50)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
    ]
