# Generated by Django 3.1.7 on 2021-04-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_applicants_resumeli'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='xyz',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
