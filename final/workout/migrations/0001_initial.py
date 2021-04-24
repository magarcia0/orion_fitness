# Generated by Django 3.0.9 on 2021-04-24 18:43

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
            name='WorkoutEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Clothing', 'Clothing'), ('Housing', 'Housing'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], max_length=128)),
                ('projected', models.IntegerField()),
                ('actual', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
