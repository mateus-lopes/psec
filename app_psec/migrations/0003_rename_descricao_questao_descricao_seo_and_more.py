# Generated by Django 4.0 on 2021-12-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_psec', '0002_alter_questao_descricao_alter_questao_numero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questao',
            old_name='descricao',
            new_name='descricao_seo',
        ),
        migrations.AddField(
            model_name='atividade',
            name='descricao_seo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]