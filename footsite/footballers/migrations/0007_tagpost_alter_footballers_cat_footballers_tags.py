# Generated by Django 5.0.6 on 2024-07-25 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballers', '0006_alter_footballers_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='footballers',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='footballers.category'),
        ),
        migrations.AddField(
            model_name='footballers',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='footballers.tagpost'),
        ),
    ]
