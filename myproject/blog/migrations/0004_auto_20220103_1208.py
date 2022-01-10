# Generated by Django 3.2.10 on 2022-01-03 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220103_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childern', to='blog.category', verbose_name='زیردسته'),
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=1, verbose_name='پوزیشن'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=256, unique=True, verbose_name='آدرس دسته بندی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.Category'),
        ),
    ]