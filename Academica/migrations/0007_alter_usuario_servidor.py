# Generated by Django 3.2.5 on 2021-07-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0006_alter_jugador_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='servidor',
            field=models.CharField(max_length=6),
        ),
    ]
