# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Idc(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'供应商名称')
    webstie = models.CharField(max_length=40, verbose_name=u'供应商网站')
    create_time = models.DateField(verbose_name=u'创建时间')
    status = models.IntegerField(verbose_name=u'使用状态')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'供应商列表'
        verbose_name_plural = u'供应商列表'

class Host(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'主机名称')
    ip = models.GenericIPAddressField(unique=True, verbose_name=u'IP地址')
    address_name = models.CharField(max_length=40, verbose_name=u'主机所在机房')
    purpose = models.CharField(max_length=40, verbose_name=u'主机用途')
    idc_name = models.CharField(max_length=40, verbose_name=u'主机所在供应商')
    idc_contact = models.CharField(max_length=40, verbose_name=u'主机供应商联系方式')
    create_time = models.DateField(verbose_name=u'创建时间')
    due_time = models.DateField(verbose_name=u'过期时间')
    status = models.IntegerField(verbose_name=u'使用状态')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'主机列表'
        verbose_name_plural = u'主机列表'

class User(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'用户名称')
    password = models.CharField(max_length=40, verbose_name=u'用户密码')
    nickname = models.CharField(max_length=40, verbose_name=u'用户别名')
    departname = models.CharField(max_length=40, verbose_name=u'用户所在部门名称')
    email = models.CharField(max_length=40, verbose_name=u'用户电邮')
    register_time = models.DateField(verbose_name=u'创建用户时间')
    status = models.IntegerField(verbose_name=u'使用状态')
    last_ip = models.CharField(max_length=40, verbose_name=u'用户最后登录IP')
    last_time = models.DateField(verbose_name=u'用户最后登录时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'用户列表'
        verbose_name_plural = u'用户列表'

class Order(models.Model):
    hostname = models.CharField(max_length=40, verbose_name=u'主机名称')
    username = models.CharField(max_length=40, verbose_name=u'用户名称')
    bank_id = models.CharField(max_length=40, verbose_name=u'银行账号')
    bank_name = models.CharField(max_length=40, verbose_name=u'银行名称')
    start_time = models.DateField(verbose_name=u'申请时间')
    due_time = models.DateField(verbose_name=u'截止时间')
    pay_status = models.IntegerField(verbose_name=u'付款状态')
    examine_status = models.IntegerField(verbose_name=u'审核状态')
    status = models.IntegerField(verbose_name=u'申请单状态')

    def __unicode__(self):
        return self.hostname


    class Meta:
        verbose_name = u'订单列表'
        verbose_name_plural = u'订单列表'
# Create your models here.
