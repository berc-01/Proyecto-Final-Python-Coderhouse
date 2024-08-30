# Generated by Django 5.1 on 2024-08-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_marca2_monitores_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coolers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('altura', models.CharField(max_length=40)),
                ('ventilador', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('capacidad', models.CharField(max_length=40)),
                ('velocidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('serie', models.CharField(max_length=40)),
                ('memoria', models.CharField(max_length=40)),
                ('largo', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='monitores',
            name='hercios',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monitores',
            name='resolucion',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procesadores',
            name='frecuencia',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procesadores',
            name='hilos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procesadores',
            name='nucleos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]