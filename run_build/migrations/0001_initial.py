# Generated by Django 2.2.1 on 2019-05-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('blog_text', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
