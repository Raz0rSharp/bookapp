# Generated by Django 3.1.7 on 2021-03-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
                ('photo', models.ImageField(upload_to=None)),
                ('price', models.FloatField()),
            ],
        ),
    ]
