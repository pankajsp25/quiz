# Generated by Django 3.1.1 on 2020-09-17 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('correct_ans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.option')),
                ('options', models.ManyToManyField(to='quiz.Option')),
            ],
        ),
    ]
