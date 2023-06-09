# Generated by Django 4.0.5 on 2023-03-29 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('ID', models.TextField(primary_key=True, serialize=False)),
                ('Title', models.TextField()),
                ('Author', models.TextField()),
                ('Publisher', models.TextField()),
                ('Filter_number', models.IntegerField()),
                ('All_filter', models.TextField()),
                ('Y_date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MARK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.book')),
            ],
        ),
    ]
