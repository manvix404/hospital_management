# Generated by Django 3.2.9 on 2021-11-20 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospmanagement', '0002_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('specialization', models.CharField(max_length=50)),
                ('patient_email', models.EmailField(max_length=100)),
                ('patient_phone', models.CharField(max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospmanagement.doctor')),
            ],
        ),
    ]
