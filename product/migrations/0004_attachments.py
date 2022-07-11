# Generated by Django 3.0.7 on 2022-02-05 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_auto_20211230_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=120)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded On')),
                ('attachment', models.FileField(max_length=1001, upload_to='attachments/%Y/%m/')),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attachment_uploaded_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
