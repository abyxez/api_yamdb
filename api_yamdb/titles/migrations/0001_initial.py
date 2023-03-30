<<<<<<< HEAD
# Generated by Django 3.2 on 2023-03-29 19:42

from django.conf import settings
=======
# Generated by Django 3.2 on 2023-03-30 13:21

>>>>>>> feature/models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> feature/models
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Category name')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Genre name')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('year', models.DateField(verbose_name='Publication year')),
<<<<<<< HEAD
                ('description', models.TextField(verbose_name='Description')),
=======
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
>>>>>>> feature/models
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='titles', to='titles.category', verbose_name='Slug of category')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='titles', to='titles.genre', verbose_name='Slug of genre')),
            ],
            options={
                'default_related_name': 'titles',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text of the review')),
                ('score', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Rating score')),
<<<<<<< HEAD
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
=======
>>>>>>> feature/models
                ('title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='titles.title')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
<<<<<<< HEAD
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
=======
>>>>>>> feature/models
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='titles.review')),
                ('title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='titles.title')),
            ],
            options={
                'default_related_name': 'comments',
            },
        ),
    ]
