# Generated by Django 4.1.3 on 2022-11-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_alter_cliente_foto_alter_emprestimo_aprovacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto',
        ),
    ]