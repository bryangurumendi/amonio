# Generated by Django 3.0.5 on 2020-05-02 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20200502_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sector',
            field=models.CharField(choices=[('sur', 'Sur'), ('sur_e', 'Sur-Este'), ('cen', 'Centro'), ('nor', 'Norte'), ('samb', 'Samborondon')], max_length=50, verbose_name='sector'),
        ),
    ]
