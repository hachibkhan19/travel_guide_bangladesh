# Generated by Django 3.0.2 on 2020-01-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0003_barishal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Khulna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='khul_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Mymensingh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='my_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Rajshahi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='raj_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Rangpur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='rang_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Sylhet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='sylh_pic')),
            ],
        ),
    ]
