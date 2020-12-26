# Generated by Django 3.1.4 on 2020-12-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name_plural': 'Todo'},
        ),
    ]