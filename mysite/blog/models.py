# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Tkconstants import CASCADE

from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.


class Account(models.Model):
    username      = models.CharField(unique=True, max_length=80)
    password      = models.CharField(max_length=80)
    name          = models.CharField(max_length=120)
    CHOICE_SEX    = (('M', 'Men'),('W', 'Women'))
    sex           = models.CharField(max_length=1, choices=CHOICE_SEX)
    birtday       = models.DateField()
    address       = models.CharField(max_length=200)
    phone         = models.CharField(max_length=13)
    email         = models.EmailField(unique=True)
    CHOICE_TYPE   = (('1', 'Admin'),('2', 'Author'),('3', 'Manager'),('4', 'Staff'))
    type_account  = models.CharField(choices=CHOICE_TYPE, max_length=1, default= 4)
    date_register = models.DateTimeField(auto_now_add=True)
    CHOICE_ACTION = (('1', 'True'),('0', 'False'))
    active        = models.CharField(choices=CHOICE_ACTION, max_length=1, default=0)
    key           = models.CharField(max_length=200)
    online        = models.BooleanField(default=False)
    avatar        = models.ImageField(upload_to='avatar/')
    def __str__(self):
        return self.name

class Catalog(models.Model):
    name            = models.CharField(max_length=100)
    unsigned_name   = models.CharField(max_length=200)
    order_sort      = models.IntegerField()
    CHOICE_PUBLIC   = (('1', 'True'), ('0', 'False'))
    public          = models.CharField(default=0, max_length=1, choices=CHOICE_PUBLIC)
    meta_desc       = models.CharField(max_length=120)
    meta_key        = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name            = models.CharField(max_length=200)
    unsigned_name   = models.CharField(max_length=200)
    created         = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Posts(models.Model):
    title               = models.CharField(max_length=200)
    unsigned_title      = models.CharField(max_length=250)
    excerpt             = models.TextField()
    image               = models.ImageField(upload_to='posts/')
    date                = models.DateTimeField(auto_now_add=True)
    id_user             = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name ='Author')
    content             = models.TextField()
    id_catalog          = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Catalog')
    view                = models.IntegerField(default=0, verbose_name ='View')
    tag                 = models.ManyToManyField(Tag, related_name='posts')
    pre_post            = models.IntegerField(verbose_name='Preview Post')
    next_post           = models.IntegerField(verbose_name='Next Post')
    CHOICE_HIGHLIGHT    = (('1', 'True'), ('0', 'False'))
    highlight           = models.CharField(default=0, max_length=1, choices=CHOICE_HIGHLIGHT)
    CHOICE_PUBLIC       = (('1', 'Public'), ('0', 'Private'))
    public              = models.CharField(default=1, max_length=1, choices=CHOICE_PUBLIC)
    def __str__(self):
        return self.title


class Comment(models.Model):
    name            = models.CharField(max_length=120)
    image           = models.URLField(blank=True)
    email           = models.EmailField()
    website         = models.URLField(blank=True)
    content         = models.TextField()
    date            = models.DateTimeField(auto_now_add=True)
    id_post         = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Post')
    CHOICE_PUBLIC   = (('1','True'),('0', 'False'))
    public          = models.FileField(default=1, choices=CHOICE_PUBLIC, max_length=1)

    def __str__(self):
        return self.name

