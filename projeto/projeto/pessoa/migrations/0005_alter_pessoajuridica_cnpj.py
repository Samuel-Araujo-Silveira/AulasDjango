# Generated by Django 5.0.4 on 2024-05-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_pessoajuridica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoajuridica',
            name='cnpj',
            field=models.CharField(max_length=100),
        ),
    ]