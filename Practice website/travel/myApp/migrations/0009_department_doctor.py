# Generated by Django 3.0.5 on 2023-10-13 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20231012_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='departments/')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=70)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Department')),
            ],
        ),
    ]
