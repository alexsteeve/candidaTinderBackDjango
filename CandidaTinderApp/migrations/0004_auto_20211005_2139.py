# Generated by Django 3.2.7 on 2021-10-05 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CandidaTinderApp', '0003_auto_20211005_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='IdParlamentar1',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='IdParlamentar2',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='IdParlamentar3',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='IdPartido1',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='IdPartido2',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='IdPartido3',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='PercentualParlamentar1',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='PercentualParlamentar2',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='PercentualParlamentar3',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='PercentualPartido1',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='PercentualPartido2',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='PercentualPartido3',
        ),
        migrations.CreateModel(
            name='PartidoUsuario',
            fields=[
                ('IdPartidoUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('OrdemAfinidade', models.IntegerField(default=0)),
                ('PercentualPartido', models.IntegerField(default=0)),
                ('IdPartido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidaTinderApp.partidos')),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidaTinderApp.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatoUsuario',
            fields=[
                ('IdCandidatoUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('OrdemAfinidade', models.IntegerField(default=0)),
                ('PercentualParlamentar', models.IntegerField(default=0)),
                ('IdParlamentar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidaTinderApp.parlamentares')),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CandidaTinderApp.usuarios')),
            ],
        ),
    ]