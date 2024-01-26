# Generated by Django 4.0.5 on 2023-02-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_project_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.IntegerField(unique=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]