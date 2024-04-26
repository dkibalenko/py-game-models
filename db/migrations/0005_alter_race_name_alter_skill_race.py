# Generated by Django 4.0.2 on 2024-04-25 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(choices=[('elf', 'The elf race'), ('dwarf', 'The dwarf race'), ('human', 'Human race'), ('ork', 'The ork race')], max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='db.race'),
        ),
    ]
