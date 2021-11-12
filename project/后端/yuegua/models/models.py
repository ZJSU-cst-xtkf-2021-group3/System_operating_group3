from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table='User'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    UID=models.AutoField("用户ID",primary_key=True)
    Uname=models.CharField("用户名",max_length=50,default='unnamed')
    Passwd=models.CharField("密码",max_length=25,default='password-not-set')
    isEDIT=models.IntegerField("是否为编辑",default=0)
    header=models.ImageField("用户头像",upload_to='userHeader',default='/static/img/default.png')
    AgeRange=models.IntegerField("年龄段")
    rank=models.IntegerField("用户等级")
    public=models.IntegerField("是否仅关注后可见")
    public_Ftopic=models.IntegerField("是否展示关注的话题")
    public_Fuser = models.IntegerField("是否展示关注的人")
    public_comments=models.IntegerField("是否展示发表的评论")
    public_events=models.IntegerField("是否发表的报料")
    public_topics=models.IntegerField("是否展示发表的话题")
    introduction=models.TextField("个人介绍")
    wechatID=models.CharField("微信ID",max_length=30,default='WeiChatID-not-set')
    EXP=models.IntegerField("经验值")
    def __str__(self):
        return '用户ID:%s 用户名:%s 密码:%s 是否为编辑:%s 用户等级:%s 经验值:%s'\
               %(self.UID,self.Uname,self.Passwd,self.isEDIT,self.rank,self.EXP)





