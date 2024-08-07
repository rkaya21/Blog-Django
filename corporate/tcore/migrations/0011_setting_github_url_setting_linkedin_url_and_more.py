# Generated by Django 5.0.6 on 2024-07-05 10:25

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0010_setting_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='github_url',
            field=models.URLField(default='exit', max_length=255, verbose_name='Github'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='linkedin_url',
            field=models.URLField(default='exit', max_length=255, verbose_name='LinkedIn'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='about',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='about',
            name='content_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title_tr',
            field=models.CharField(max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcore.category', verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs', verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_tr',
            field=models.CharField(max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_tr',
            field=models.CharField(max_length=200, null=True, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='Ad Soyad'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_tr',
            field=models.CharField(max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.TextField(verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Şehir'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='description_tr',
            field=models.CharField(max_length=255, null=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='district',
            field=models.CharField(max_length=50, verbose_name='İlçe'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram_url',
            field=models.URLField(max_length=255, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keywords',
            field=models.CharField(max_length=255, verbose_name='Kelimeler'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keywords_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kelimeler'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keywords_tr',
            field=models.CharField(max_length=255, null=True, verbose_name='Kelimeler'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone_fixed',
            field=models.CharField(max_length=15, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone_mobile',
            field=models.CharField(max_length=15, verbose_name='Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='Posta Kodu'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title_tr',
            field=models.CharField(max_length=255, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='sliders', verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
    ]
