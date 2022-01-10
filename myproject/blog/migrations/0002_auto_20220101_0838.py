# Generated by Django 3.2.10 on 2022-01-01 05:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=100, unique=True, verbose_name='آدرس عنوان'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'منشر شده'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
    ]