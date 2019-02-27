from django.db import models

# Create your models here.
# 此处的 Stu 默认对应的 app_stu 表
class Stu(models.Model):
  #id = models.AutoField(primary_key=True), # 主键可以不写
  name = models.CharField(max_length=16),
  age = models.SmallIntegerField(),
  sex = models.CharField(max_length=1),
  classid = models.CharField(max_length=8)

  # 快捷输出
  def __str__():
    return "%d:%s:%d:%s:%s"%(self.id, self.name, self.age, self.sex, self.classid)
  
  # 自定义对应的表名，默认表名：app_stu
  class Meta:
    db_table='stu'