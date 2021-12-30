# Generated by Django 3.0.7 on 2021-09-19 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='country.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='country.District'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='province',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='country.Province'),
            preserve_default=False,
        ),
    ]
