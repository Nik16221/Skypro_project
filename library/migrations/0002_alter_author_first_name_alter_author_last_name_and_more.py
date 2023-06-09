# Generated by Django 4.1.7 on 2023-03-26 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='total_instances',
            field=models.PositiveIntegerField(verbose_name='всего книг в библиотеке'),
        ),
        migrations.AlterField(
            model_name='book',
            name='total_page',
            field=models.PositiveIntegerField(verbose_name='количество страниц'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='status',
            field=models.CharField(choices=[('активен', 'Is Active'), ('не активен', 'Not Active')], default='активен', max_length=10, verbose_name='статус активности'),
        ),
    ]
