# Generated by Django 5.0.7 on 2024-08-07 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('expense_type', models.CharField(choices=[('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')], max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.currentbalance')),
            ],
        ),
    ]
