# Generated by Django 3.0.1 on 2020-02-23 14:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20200218_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Статус питомца')),
                ('code', models.CharField(max_length=256, verbose_name='Код')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.PetStatus', verbose_name='Статус питомца'),
        ),
    ]