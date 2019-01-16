# Generated by Django 2.1.3 on 2019-01-16 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0018_auto_20181230_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria_problema',
            name='origem',
            field=models.CharField(max_length=50, null=True, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='local',
            field=models.CharField(choices=[('LOCAL', 'LOCAL'), ('Àrea de Vendas', 'Àrea de Vendas'), ('CPD', 'CPD'), ('Tesouraria', 'Tesouraria'), ('Gerência', 'Gerência'), ('Departamento Pessoal', 'Departamento Pessoal'), ('Deposito', 'Deposito'), ('Açougue', 'Açougue'), ('Padaria', 'Padaria'), ('Salgados', 'Salgados'), ('Açougue', 'Açougue'), ('Hortifruti', 'Hortifruti'), ('Laticínios', 'Laticínios')], default='LOCAL', max_length=100, verbose_name='LOCAL'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='status_chamado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Status_Chamado', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='unidade',
            field=models.CharField(choices=[('UNIDADE', 'UNIDADE'), ('Filial 01', 'Filial 01'), ('Filial 02', 'Filial 02'), ('Filial 03', 'Filial 03'), ('Filial 04', 'Filial 04'), ('Filial 05', 'Filial 05'), ('Filial 06', 'Filial 06'), ('Filial 07', 'Filial 07'), ('Filial 08', 'Filial 08'), ('Filial 09', 'Filial 09'), ('Filial 10', 'Filial 10'), ('Filial 11', 'Filial 11'), ('Filial 12', 'Filial 12'), ('Filial 13', 'Filial 13'), ('Filial 15', 'Filial 15'), ('Filial 16', 'Filial 16'), ('Carga Seca', 'Carga Seca'), ('Carga Fria', 'Carga Fria'), ('Città América', 'Città América'), ('Downtown', 'Downtown')], default='UNIDADE', max_length=100, verbose_name='Unidade'),
        ),
    ]
