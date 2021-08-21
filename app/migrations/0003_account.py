# Generated by Django 3.1.2 on 2021-08-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_payments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('balance', models.IntegerField()),
            ],
        ),
    ]
