from django.db import models

# Create your models here.
class Department(models.Model):
    """部门类"""

    # 部门名称：字符串类型(必须要指定最大长度)
    name = models.CharField(max_length=20)
    # 部门成立时间: 日期类型
    create_date = models.DateField(auto_now_add=True)
    # 逻辑删除标识：标识部门是否删除
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        # 指定表名
        db_table = 'department'

class Employee(models.Model):
    """员工类"""

    choices_gender = (
        (0, '男'),
        (1, '女'),
    )

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.IntegerField(default=0, choices=choices_gender)
    # 工资：浮点类型（必须要指定两个选项）  999999.99
    salary = models.DecimalField(max_digits=8, decimal_places=2,default=0.0)
    # 备注信息: 可以为空
    comment = models.CharField(max_length=300, null=True, blank=True,default="傻逼")
    # 员工入职时间
    hire_date = models.DateField(auto_now_add=True)
    # 一对多的外键：员工所属部门 department_id
    # department = models.ForeignKey('Department')
    hometown = models.CharField(max_length=30,default="福建")




    def __str__(self):
        return self.name

    class Meta:
        # 指定表名
        db_table = 'employees'