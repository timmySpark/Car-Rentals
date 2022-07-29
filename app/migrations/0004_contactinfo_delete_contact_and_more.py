# Generated by Django 4.0.4 on 2022-07-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_book_drop_off_date_alter_book_pick_up_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_icon', models.CharField(max_length=200)),
                ('detail_subject', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Contact Info',
                'verbose_name_plural': 'Contact Information',
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='detail_icon',
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='detail_subject',
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='details',
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='email',
            field=models.EmailField(default='JD@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='message',
            field=models.TextField(default='Hello There'),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='name',
            field=models.CharField(default='John Doe', max_length=100),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='subject',
            field=models.CharField(default='Greetings', max_length=100),
        ),
    ]
