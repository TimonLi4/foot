# Generated by Django 5.0.6 on 2024-07-26 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballers', '0007_tagpost_alter_footballers_cat_footballers_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='footballers',
            name='wife',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wif', to='footballers.wife'),
        ),
    ]
