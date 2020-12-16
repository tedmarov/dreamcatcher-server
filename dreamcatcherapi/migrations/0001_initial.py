# Generated by Django 3.1.4 on 2020-12-15 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('dream_story', models.CharField(max_length=3000)),
                ('date', models.DateField(auto_now_add=True)),
                ('private', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DreamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(max_length=500)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='MoonPhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Stress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stress_event', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DreamMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.dream')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.medication')),
            ],
        ),
        migrations.CreateModel(
            name='DreamcatcherUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('profile_photo', models.URLField()),
                ('bio', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dream',
            name='dream_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.dreamtype'),
        ),
        migrations.AddField(
            model_name='dream',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.exercise'),
        ),
        migrations.AddField(
            model_name='dream',
            name='moon_phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.moonphase'),
        ),
        migrations.AddField(
            model_name='dream',
            name='stress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.stress'),
        ),
        migrations.AddField(
            model_name='dream',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.dreamcatcheruser'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('dream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.dream')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamcatcherapi.dreamcatcheruser')),
            ],
        ),
    ]
