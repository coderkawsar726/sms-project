# Generated by Django 5.0.3 on 2024-04-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadminmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffinfo',
            name='staff_id',
            field=models.CharField(default='STFF8798', max_length=8, unique=True, verbose_name='Staff ID (Generated)'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Student_id',
            field=models.CharField(default='MGSD8798', max_length=8, unique=True, verbose_name='Student ID (Genereated)'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='teacher_id',
            field=models.CharField(default='TCHR8798', max_length=8, unique=True, verbose_name='Teacher ID (Generated)'),
        ),
    ]