# Generated by Django 4.0.4 on 2022-05-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30, null=True, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
    ]
