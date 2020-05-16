# Generated by Django 3.0.5 on 2020-05-02 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Function', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=128)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Function.BookInfo')),
            ],
        ),
    ]