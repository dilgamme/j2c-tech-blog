# Generated by Django 2.1 on 2020-05-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contactus_submitted_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=1000)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('SN', 'Seen'), ('UN', 'Unseen')], default='UN', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]