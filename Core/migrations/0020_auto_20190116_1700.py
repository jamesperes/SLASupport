# Generated by Django 2.1.5 on 2019-01-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0019_auto_20190116_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status_chamado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Status_Chamado', verbose_name='Status'),
        ),
    ]
