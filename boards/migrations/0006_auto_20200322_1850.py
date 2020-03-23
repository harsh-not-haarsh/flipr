# Generated by Django 3.0.3 on 2020-03-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_board_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='lists',
            field=models.ManyToManyField(blank=True, related_name='list', to='boards.List'),
        ),
    ]