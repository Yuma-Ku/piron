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
    
    def __str__(self):
        return str(id) + name


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    post_category_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    media_path = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'post'


class PostCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'post_category'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'user'
    
    def __str__(self):
        return str(self.id) + ", " + self.name + ", " + self.login_id 



class UserCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_category'


class UserFollower(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    follower_user_id = models.IntegerField()
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_follower'


class UserPostCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    post_category_id = models.IntegerField()
    created = models.CharField(max_length=255)
    updated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_post_category'
