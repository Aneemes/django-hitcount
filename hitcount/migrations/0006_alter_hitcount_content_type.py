# Generated by Django 4.2.7 on 2023-11-14 14:58

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("hitcount", "0005_auto_20230710_1843"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hitcount",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="content_type_set_for_%(class)s",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name='hitcount',
            name='object_pk',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='object ID'),
        ),
    ]
