# Generated by Django 3.0.5 on 2020-05-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20200502_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='ciudad',
            field=models.CharField(blank=True, choices=[('gye', 'Guayaquil')], max_length=50, verbose_name='ciudad'),
        ),
    ]