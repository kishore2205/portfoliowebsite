# Generated by Django 5.2.3 on 2025-07-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_id', models.PositiveIntegerField(unique=True)),
                ('visitor_name', models.CharField(max_length=100)),
                ('visitor_email', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('reason', models.TextField()),
                ('designated_attendee', models.CharField(max_length=100)),
                ('document', models.FileField(blank=True, null=True, upload_to='visitor_documents/')),
            ],
        ),
    ]
