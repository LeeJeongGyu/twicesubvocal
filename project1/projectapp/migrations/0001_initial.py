# Generated by Django 2.2.1 on 2019-05-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('birth', models.DateTimeField()),
                ('nationality', models.CharField(choices=[('K', 'Korea'), ('J', 'Japan'), ('T', 'Taiwan')], max_length=6)),
                ('position', models.TextField(choices=[('LV', 'Lead vocal'), ('LD', 'Lead dance'), ('SV', 'Sub vocal'), ('MD', 'Main dance'), ('L', 'Leader'), ('LR', 'Lead Rapper'), ('MR', 'Main Rapper')])),
            ],
        ),
    ]
