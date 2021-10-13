# Generated by Django 3.2.7 on 2021-10-04 10:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('card_id', models.IntegerField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField(default=1)),
                ('related_students', models.ManyToManyField(to='dbApp.Students')),
            ],
            options={
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
