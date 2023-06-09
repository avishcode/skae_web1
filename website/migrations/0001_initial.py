# Generated by Django 4.2 on 2023-04-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDemoPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='web/book_demo')),
            ],
        ),
        migrations.CreateModel(
            name='CareerPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='web/career')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='web/career')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, upload_to='web/img')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentTestimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.FileField(blank=True, upload_to='testimonials')),
                ('name', models.CharField(max_length=200)),
                ('batch', models.CharField(max_length=100)),
                ('rating', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('company_logo', models.ImageField(blank=True, upload_to='company_logo')),
                ('com_post', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, upload_to='web/team_members')),
                ('profile', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
