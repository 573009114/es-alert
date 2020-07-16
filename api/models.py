 # -*- coding: utf-8 -*-
from django.db import models

class EsAlertMembers(models.Model):
    '''
    联系人模型
    '''
    name = models.CharField(max_length=128) 
    tel = models.CharField(max_length=11, verbose_name="手机号", default="")
    email=models.EmailField('邮箱',max_length=50,unique=True)
    
    class Meta:
        db_table = 'es_alert_members' 

class EsAlertGroups(models.Model):
    '''
    告警组模型
    '''
    group_name = models.CharField(max_length=128,null=False)
    member = models.ForeignKey(EsAlertMembers,on_delete=models.CASCADE)
    class Meta:
        db_table = 'es_alert_group'
    
class EsAlertRules(models.Model):
    '''
    告警规则模型
    '''
    name = models.CharField(max_length=128)
    es_index_prefix = models.CharField(max_length=128)
    es_query = models.CharField(max_length=128)
    log_count = models.IntegerField()
    in_minutes = models.IntegerField()
    trigger = models.IntegerField(blank=True, null=True)
    product = models.CharField(max_length=128)
    priority = models.IntegerField()
    no_deal = models.IntegerField()
    owner = models.CharField(max_length=128)
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'es_alert_rules'

# 应用注册
class AppType(models.Model):
    name = models.CharField(max_length=128,unique=True)
    url = models.CharField(max_length=128,unique=True)
    event  = models.CharField(max_length=128,unique=True)
    class Meta:
        db_table = 'es_app_type'

# 数据源模型
class DataSource(models.Model):
    app_name = models.CharField(max_length=128,unique=True)
    app_source = models.CharField(max_length=32)

    class Meta:
        db_table = 'es_data_source'

class DataSourceTemplate(models.Model):
    app_name = models.CharField(max_length=32,unique=True)
    app_source = models.CharField(max_length=128)

    class Meta:
        db_table = 'es_data_source_template'

# 仪表盘模型
class DashboardEvent(models.Model):
    last_time =  models.DateTimeField()
    event_name = models.CharField(max_length=32)
    event_describe =  models.CharField(max_length=128)
    class Meta:
        db_table = 'es_dashboard_event'

# 系统设置模型

class SystemSetting(models.Model):
    website_name = models.CharField(max_length=32)
    email = models.EmailField('邮箱',max_length=50,unique=True)
    
    class Meta:
        db_table = 'es_system_setting'

    