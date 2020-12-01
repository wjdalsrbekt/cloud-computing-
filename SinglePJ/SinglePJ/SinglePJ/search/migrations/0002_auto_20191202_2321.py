# Generated by Django 2.2.7 on 2019-12-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchList',
            fields=[
                ('code', models.IntegerField(db_column='CODE', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='TITLE', max_length=200, null=True)),
                ('price', models.CharField(blank=True, db_column='PRICE', max_length=20, null=True)),
            ],
            options={
                'db_table': 'search_list',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='search',
        ),
    ]
