# Generated by Django 4.0.2 on 2022-02-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evernote', '0004_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='VisitCount',
        ),
    ]