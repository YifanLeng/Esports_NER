# Generated by Django 2.2.6 on 2019-12-04 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=10000)),
                ('game', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=100)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crf_predict.Doc')),
            ],
        ),
    ]
