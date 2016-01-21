# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentItem',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iring.Item')),
                ('content', models.TextField()),
            ],
            bases=('iring.item',),
        ),
        migrations.CreateModel(
            name='FileItem',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iring.Item')),
                ('size', models.BigIntegerField()),
            ],
            bases=('iring.item',),
        ),
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iring.Item')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
            bases=('iring.item',),
        ),
        migrations.AddField(
            model_name='item',
            name='board',
            field=models.ForeignKey(to='iring.models.Collection'),
        ),
    ]
