# Generated by Django 3.1.7 on 2021-04-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210426_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='resumeli',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]