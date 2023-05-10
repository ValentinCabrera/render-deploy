# Generated by Django 4.1.2 on 2023-03-18 06:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_alter_pedido_fecha_listo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_emision',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_listo',
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]