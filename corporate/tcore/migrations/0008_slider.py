# Generated by Django 5.0.6 on 2024-07-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0007_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='sliders')),
            ],
        ),
    ]
