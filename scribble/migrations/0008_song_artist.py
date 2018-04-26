# Generated by Django 2.0.4 on 2018-04-25 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scribble', '0007_auto_20180425_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='scribble.Artist'),
            preserve_default=False,
        ),
    ]