# Generated by Django 3.1.14 on 2022-06-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0008_auto_20220613_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='related_tags',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags_product', to='shops.Tagmodel'),
        ),
    ]
