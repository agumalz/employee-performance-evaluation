# Generated by Django 5.0.6 on 2024-08-12 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0005_delete_nilaikriteria'),
        ('perhitungan_fuzzy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerhitunganFuzzy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasil_akhir', models.FloatField()),
                ('kinerja', models.CharField(max_length=10)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew.crew')),
            ],
        ),
    ]
