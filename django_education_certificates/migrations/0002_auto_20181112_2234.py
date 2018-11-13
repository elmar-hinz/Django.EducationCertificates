# Generated by Django 2.1.3 on 2018-11-12 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_education_certificates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('rank', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('rank',),
            },
        ),
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ('rank',)},
        ),
        migrations.AddField(
            model_name='certificate',
            name='category',
            field=models.ManyToManyField(to='django_education_certificates.Category'),
        ),
    ]
