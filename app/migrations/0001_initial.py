# Generated by Django 5.1.7 on 2025-03-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth_data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('year', models.IntegerField(default=1900)),
                ('genre', models.TextField()),
                ('actors', models.ManyToManyField(related_name='actors', to='app.actors')),
            ],
        ),
    ]
