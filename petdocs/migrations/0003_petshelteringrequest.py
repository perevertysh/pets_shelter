# Generated by Django 3.0.1 on 2020-02-23 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('petdocs', '0002_auto_20191222_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetShelteringRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
    ]
