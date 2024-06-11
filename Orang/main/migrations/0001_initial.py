# Generated by Django 5.0.6 on 2024-06-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id_children', models.AutoField(primary_key=True, serialize=False)),
                ('famili_ch', models.CharField(max_length=100)),
                ('name_ch', models.CharField(max_length=100)),
                ('last_name_ch', models.CharField(max_length=100)),
                ('pol', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('adress_ch', models.CharField(max_length=100)),
                ('telephone_ch', models.CharField(max_length=100)),
                ('ychastie', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'children',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupa',
            fields=[
                ('id_groupa', models.AutoField(primary_key=True, serialize=False)),
                ('number_gr', models.IntegerField()),
                ('vozrast', models.IntegerField()),
                ('count_sportsmenov', models.IntegerField()),
            ],
            options={
                'db_table': 'groupa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Razriad',
            fields=[
                ('id_razriad', models.AutoField(primary_key=True, serialize=False)),
                ('razriad', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'razriad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roditel',
            fields=[
                ('id_roditel', models.AutoField(primary_key=True, serialize=False)),
                ('famili_ro', models.CharField(max_length=100)),
                ('name_ro', models.CharField(max_length=100)),
                ('last_name_ro', models.CharField(max_length=100)),
                ('telephone_ro', models.TextField()),
                ('adress', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'roditel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sorevnovania',
            fields=[
                ('id_sorevnovania', models.AutoField(primary_key=True, serialize=False)),
                ('name_so', models.CharField(max_length=100)),
                ('place_so', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('rezult', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sorevnovania',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trenera',
            fields=[
                ('id_trenera', models.AutoField(primary_key=True, serialize=False)),
                ('famili_tr', models.CharField(max_length=100)),
                ('name_tr', models.CharField(max_length=100)),
                ('last_name_tr', models.CharField(max_length=100)),
                ('spesalaize', models.CharField(max_length=100)),
                ('date_tr', models.DateField()),
                ('pasport_t', models.CharField(max_length=100)),
                ('adress_t', models.CharField(max_length=100)),
                ('telephone_t', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'trenera',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VidSporta',
            fields=[
                ('id_vid_sporta', models.AutoField(primary_key=True, serialize=False)),
                ('vid_sporta', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vid_sporta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zvanie',
            fields=[
                ('id_zvanie', models.AutoField(primary_key=True, serialize=False)),
                ('zvanie', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'zvanie',
                'managed': False,
            },
        ),
    ]