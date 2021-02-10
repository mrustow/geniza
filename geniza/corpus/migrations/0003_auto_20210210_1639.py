# Generated by Django 3.1.6 on 2021-02-10 21:39

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('corpus', '0002_create_languagescript'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('old_input_by', models.CharField(help_text='Legacy input information from Google Sheets', max_length=255)),
                ('old_input_date', models.CharField(help_text='Legacy input date from Google Sheets', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelfmark', models.CharField(max_length=255)),
                ('old_shelfmarks', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, help_text="Link to library's catalog record for this fragment.", verbose_name='URL')),
                ('iiif_url', models.URLField(blank=True, verbose_name='URL')),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('library', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corpus.library')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_block', models.CharField(max_length=255)),
                ('multifragment', models.CharField(max_length=255)),
                ('side', models.CharField(blank=True, choices=[('r', 'Recto'), ('v', 'Verso'), ('rv', 'Recto and Verso')], max_length=255)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpus.document')),
                ('fragment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpus.fragment')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='doctype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corpus.documenttype'),
        ),
        migrations.AddField(
            model_name='document',
            name='fragments',
            field=models.ManyToManyField(through='corpus.DocumentFragment', to='corpus.Fragment'),
        ),
        migrations.AddField(
            model_name='document',
            name='languages',
            field=models.ManyToManyField(blank=True, to='corpus.LanguageScript'),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
