from django.db import models
#user_login, user_details, user_pic, user_posts, pic_pool, type_master, keywords_master, user_post_keyword_map

# Create your models here.

class user_login(models.Model):
    uname = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    profile_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    addr = models.CharField(max_length=500)
    pin = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    status = models.CharField(max_length=50)

class user_pic(models.Model):
    user_id = models.IntegerField()
    pic_path = models.CharField(max_length=250)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class user_posts(models.Model):
    user_id = models.IntegerField()
    post_type = models.CharField(max_length=500)
    msg = models.CharField(max_length=500)
    pic = models.CharField(max_length=500)
    dt = models.CharField(max_length=500)
    tm = models.CharField(max_length=500)
    status = models.CharField(max_length=500)

class pic_pool(models.Model):
    pic = models.CharField(max_length=250)
    type_id = models.IntegerField()

class type_master(models.Model):
    type_name = models.CharField(max_length=150)

class keywords_master(models.Model):
    keywords = models.CharField(max_length=250)

class user_post_keyword_map(models.Model):
    post_id = models.IntegerField()
    keyword_id = models.IntegerField()

class label_master(models.Model):
    label = models.CharField(max_length=1500)

    def __str__(self):
        return self.label

class data_set(models.Model):
    label_id = models.IntegerField()
    data_file = models.CharField(max_length=1500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.data_file

class user_review(models.Model):
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    msg = models.CharField(max_length=1500)
    dt = models.CharField(max_length=30)
    tm = models.CharField(max_length=15)