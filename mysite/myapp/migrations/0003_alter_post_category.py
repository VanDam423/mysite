# Generated by Django 4.2.8 on 2023-12-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('main', 'Главное'), ('interesting', 'Интересное'), ('politic', 'Политика'), ('economy', 'Экономика'), ('culture', 'Культура')], default='other', max_length=20),
        ),
    ]
