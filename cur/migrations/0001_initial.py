# Generated by Django 4.0.1 on 2022-02-09 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CURReport',
            fields=[
                ('manifest_key', models.CharField(max_length=1024, primary_key=True, serialize=False)),
                ('last_updated', models.DateTimeField()),
                ('storage_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.storageinfo')),
            ],
            options={
                'db_table': 'cur_report',
                'unique_together': {('storage_info', 'manifest_key')},
            },
        ),
    ]
