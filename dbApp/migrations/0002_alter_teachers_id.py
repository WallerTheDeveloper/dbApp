# Generated by Django 3.2.7 on 2021-10-04 10:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dbApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
