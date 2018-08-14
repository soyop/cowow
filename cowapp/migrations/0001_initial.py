# Generated by Django 2.0.7 on 2018-08-02 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gestation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('texte', models.TextField()),
                ('date_publication', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Senseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('mouvement', models.IntegerField(default=0)),
                ('date_stocker', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vache',
            fields=[
                ('numero_tag', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date_stocker', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('sexe', models.CharField(choices=[('F', 'Femelle'), ('M', 'Mâle')], max_length=1, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='senseur',
            name='vache',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cowapp.Vache'),
        ),
        migrations.AddField(
            model_name='gestation',
            name='vache',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cowapp.Vache'),
        ),
    ]
