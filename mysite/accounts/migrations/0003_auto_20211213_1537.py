# Generated by Django 3.1.7 on 2021-12-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211213_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.TextField(max_length=200, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_img',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media', verbose_name='Profile Image'),
        ),
    ]
