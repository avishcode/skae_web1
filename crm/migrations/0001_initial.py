# Generated by Django 4.2 on 2023-04-28 11:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, help_text='short description about the job', max_length=250)),
                ('status', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.CharField(blank=True, max_length=15)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Scheduled', 'Scheduled'), ('Selected', 'Selected'), ('Rejected', 'Rejected')], default='Applied', max_length=20)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('median_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='phone number should exactly be in 10 digits', regex='^\\d{10}$')])),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('working_exp', models.TextField()),
                ('hobbies', models.TextField()),
                ('strength', models.TextField()),
                ('weakness', models.TextField()),
                ('skills', models.TextField()),
                ('discussion_topic', models.TextField(help_text='5 favorite topic for discussion')),
                ('describe_life', models.TextField(help_text='Your Opinion about life')),
                ('describe_yourself', models.TextField(help_text='Describe Yourself')),
                ('non_judgmental', models.TextField(help_text='What do you mean by non-jugmental')),
                ('counselling', models.TextField(help_text='What do you mean by counselling')),
                ('resume', models.FileField(null=True, upload_to='Resume')),
                ('job_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.jobcategory')),
            ],
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_desc', models.TextField(max_length=300)),
                ('skill', models.CharField(max_length=300)),
                ('roles_responsibilty', models.CharField(max_length=300)),
                ('video_url', models.URLField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('job_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.jobcategory')),
            ],
        ),
        migrations.CreateModel(
            name='DemoStudentFollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('demo_st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.bookdemo')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.counsellor')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(blank=True, max_length=15)),
                ('query_status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved'), ('Hold', 'Hold')], default='Pending', max_length=20)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='phone number should exactly be in 10 digits', regex='^\\d{10}$')])),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('follow_up_note', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.counsellor')),
            ],
        ),
        migrations.CreateModel(
            name='ContactLeadFollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved'), ('Hold', 'Hold')], default='Pending', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('note', models.CharField(max_length=200)),
                ('next_followup_date', models.DateField(blank=True, null=True)),
                ('next_followup_time', models.TimeField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.contactus')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.counsellor')),
            ],
        ),
    ]
