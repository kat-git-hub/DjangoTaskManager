# Generated by Django 4.2.1 on 2023-06-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0004_alter_labels_created_at_alter_labels_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created date'),
        ),
        migrations.AlterField(
            model_name='labels',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]