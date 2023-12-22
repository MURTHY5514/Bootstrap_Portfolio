# Generated by Django 5.0 on 2023-12-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_delete_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('usn', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('college_name', models.CharField(max_length=160)),
                ('offter_status', models.CharField(max_length=60)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('proj_report', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
