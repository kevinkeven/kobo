# Generated by Django 2.2.7 on 2021-06-25 17:54

from django.db import migrations, models
import kpi.models.import_export_task
import private_storage.fields
import private_storage.storage.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0036_add_date_deleted_field_to_asset_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetfile',
            name='synced_with_backend',
            field=models.BooleanField(default=False),
        ),
    ]
