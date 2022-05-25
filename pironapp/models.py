# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    login_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    auth_flg = models.IntegerField(blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Post(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    post_category_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    media_path = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)
    icon_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_category'


class User(models.Model):
    name = models.CharField(max_length=255)
    login_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    user_category_id = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    invalid_flg = models.IntegerField(blank=True, null=True)
    allow_multiple_user_flg = models.IntegerField(blank=True, null=True)
    profile_path = models.CharField(max_length=255, blank=True, null=True)
    cover_path = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)
    setup_flg = models.IntegerField(blank=True, null=True)
    delete_flg = models.IntegerField(blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    prefecture = models.IntegerField(blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    main_area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_category'


class UserFollower(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    follower_user_id = models.IntegerField(blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_follower'


class UserPostCategory(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    post_category_id = models.IntegerField(blank=True, null=True)
    created = models.CharField(max_length=255, blank=True, null=True)
    updated = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_post_category'


class UserVerification(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    verify_flg = models.IntegerField(blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_verification'
