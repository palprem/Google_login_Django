# Generated by Django 3.1.4 on 2020-12-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(upload_to='static')),
                ('upload', models.ImageField(upload_to='static')),
            ],
        ),
        migrations.DeleteModel(
            name='dp',
        ),
    ]