# Generated by Django 4.1.1 on 2025-03-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=64)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
