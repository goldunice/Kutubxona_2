# Generated by Django 4.2.6 on 2023-10-15 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitoblari', to='asosiy.muallif'),
        ),
    ]
