# Generated by Django 2.2.4 on 2019-11-14 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.CharField(default='aluno', max_length=20),
            preserve_default=False,
        ),
    ]
