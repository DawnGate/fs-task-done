# Generated by Django 4.1.1 on 2022-10-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unity', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signupemail',
            options={'ordering': ['-add_date']},
        ),
        migrations.AddField(
            model_name='signupemail',
            name='subcriber',
            field=models.BooleanField(default=True),
        ),
    ]
