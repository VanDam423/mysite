# Generated by Django 4.2.8 on 2023-12-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('economy', 'Экономика'), ('culture', 'Культура'), ('other', 'Другое')], default='other', max_length=20),
        ),
    ]
