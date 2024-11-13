# Generated by Django 5.0.3 on 2024-05-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadminmanagement', '0005_notice_publish_category_alter_staffinfo_staff_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='active_status',
            field=models.CharField(choices=[('0', 'Save as Draft'), ('1', 'Publish')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='notice',
            name='publish_category',
            field=models.CharField(choices=[('3', 'Teachers'), ('6', 'Staffs & Teachers'), ('5', 'Students & Teachers'), ('2', 'Students'), ('1', 'All'), ('4', 'Staffs'), ('7', 'Administrations')], default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='staff_id',
            field=models.CharField(default='STFF2391', max_length=8, unique=True, verbose_name='Staff ID (Generated)'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_id',
            field=models.CharField(default='MGSD625731', max_length=10, unique=True, verbose_name='Student ID -Genereated'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='teacher_id',
            field=models.CharField(default='TCHR2391', max_length=8, unique=True, verbose_name='Teacher ID (Generated)'),
        ),
    ]