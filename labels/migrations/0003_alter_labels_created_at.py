# Generated by Django 4.2.1 on 2023-05-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_labels_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created date'),
        ),
    ]
