# Generated by Django 4.2.6 on 2023-11-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='rating',
            field=models.CharField(choices=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')], max_length=5),
        ),
    ]
