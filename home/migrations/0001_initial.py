# Generated by Django 3.1.1 on 2020-09-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Partner Adı')),
                ('image', models.ImageField(help_text='Boyutlar : 390x73', upload_to='partners/', verbose_name='Logo')),
                ('sorting', models.IntegerField(verbose_name='Sıra')),
                ('is_published', models.BooleanField(default=True, verbose_name='Yayımlama')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partnerler',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(help_text='Önerilen boyutlar: 222x108', upload_to='settings/', verbose_name='Logo')),
                ('favicon', models.ImageField(help_text='favicon.ico 16x16', upload_to='settings/', verbose_name='Favicon')),
                ('title', models.CharField(max_length=200, verbose_name='Site Adı')),
                ('keywords', models.TextField(help_text='Örn : keyword1, keyword2, keyword3, ..', verbose_name='Anahtar Kelimeler')),
                ('description', models.TextField(help_text='description', verbose_name='Açıklama Metni')),
                ('short_address', models.CharField(help_text='Semt, Şehir', max_length=25, verbose_name='Kısa Adres')),
                ('long_address', models.TextField(verbose_name='Adres')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefon Numarası')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Adresi')),
                ('facebook', models.URLField(default='https://www.facebook.com/')),
                ('instagram', models.URLField(default='https://www.instagram.com/')),
                ('twitter', models.URLField(default='https://www.twitter.com/')),
                ('linked_in', models.URLField(default='https://tr.linkedin.com/')),
                ('logo_footer', models.ImageField(help_text='Önerilen boyutlar: 222x100', upload_to='settings/', verbose_name='Footer Logo')),
            ],
            options={
                'verbose_name': 'Ayar',
                'verbose_name_plural': 'Ayarlar',
            },
        ),
    ]
