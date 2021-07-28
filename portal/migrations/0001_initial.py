# Generated by Django 3.1.5 on 2021-07-26 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, default='', upload_to='author_picture/')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('firstParagraph', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True)),
                ('slug_category', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.author')),
            ],
        ),
    ]
