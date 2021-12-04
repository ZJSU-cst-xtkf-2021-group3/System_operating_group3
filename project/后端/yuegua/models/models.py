from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table='User'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    UID=models.AutoField("用户ID",primary_key=True)
    Uname=models.CharField("用户名",max_length=25,default='unnamed')
    Passwd=models.CharField("密码",max_length=25,default='password-not-set')
    isEDIT=models.BooleanField("是否为编辑",default=False)
    header=models.ImageField("用户头像",upload_to='userHeader',default='/static/img/default.png')
    AgeRange=models.IntegerField("年龄段")
    rank=models.IntegerField("用户等级")
    introduction=models.TextField("个人介绍")
    wechatID=models.CharField("微信ID",max_length=30,default='WeiChatID-not-set')
    EXP=models.IntegerField("经验值")
    Fcounts=models.IntegerField("关注人数",default=0)
    ifPassedExam=models.BooleanField("是否通过了会员测试",default=False)
    def __str__(self):
        return '用户ID:%s 用户名:%s 密码:%s 是否为编辑:%s 用户等级:%s 经验值:%s'\
               %(self.UID,self.Uname,self.Passwd,self.isEDIT,self.rank,self.EXP)


class userPrivacy(models.Model):
    class Meta:
        db_table = 'userPrivacy'
        verbose_name = '用户空间权限'
        verbose_name_plural = '用户空间权限'

    UID=models.IntegerField("用户ID",primary_key=True)
    public = models.BooleanField("是否仅关注后可见", default=False)
    public_Ftopic = models.BooleanField("是否展示关注的话题", default=True)
    public_Fuser = models.BooleanField("是否展示关注的人", default=True)
    public_comments = models.BooleanField("是否展示发表的评论", default=True)
    public_events = models.BooleanField("是否展示发表的报料", default=True)
    public_topics = models.BooleanField("是否展示发表的话题", default=True)


class userInterests(models.Model):
    class Meta:
        db_table = 'UserInterests'
        verbose_name = '用户兴趣'
        verbose_name_plural = '用户兴趣'

    UID = models.IntegerField("用户ID")
    field=models.IntegerField("兴趣领域")

    def __str__(self):
        return '用户ID:%s 兴趣:%s '%(self.UID,self.field)

class userFollow_user(models.Model):

    class Meta:
        db_table = 'userFollow_user'
        verbose_name = '用户关注的博主'
        verbose_name_plural = '用户关注的博主'

    UID = models.IntegerField("用户ID")
    FUID = models.IntegerField("被关注人的ID")
    FUname=models.CharField("被关注人的用户名",max_length=25,default='unnamed')
    AgeRange=models.IntegerField("年龄段",default='0')
    lastVisitTime=models.IntegerField("最后访问时间戳",default=0)

    def __str__(self):
        return '用户ID:%s 被关注人的用户名:%s '%(self.UID,self.FUname)

class userFollow_topic(models.Model):

    class Meta:
        db_table = 'userFollow_topic'
        verbose_name = '用户关注的话题'
        verbose_name_plural = '用户关注的话题'

    UID = models.IntegerField("用户ID")
    FTID = models.IntegerField("被关注话题的ID")
    lastVisitTime = models.IntegerField("最后访问时间戳",default=0)



class Comments(models.Model):
    class Meta:
        db_table = 'Comments'
        verbose_name = '用户评论'
        verbose_name_plural = '用户评论'

    CID = models.AutoField("评论ID", primary_key=True)
    UID = models.IntegerField("用户ID")
    Uname=models.CharField("用户名",max_length=25,default='')
    TID = models.IntegerField("所属话题ID")
    value=models.TextField("评论内容")
    time=models.IntegerField("发布时间")
    star=models.IntegerField("点赞数")
    tip_off=models.IntegerField("举报数")
    status=models.BooleanField("显示/下架锁定",default=True)
    hotPoints=models.FloatField("热值",default=0.0)



class Topic(models.Model):

    class Meta:
        db_table = 'Topic'
        verbose_name = '话题'
        verbose_name_plural = '话题'

    TID = models.AutoField("话题ID", primary_key=True)
    UID = models.IntegerField("发布者ID")
    category=models.IntegerField("话题所属类别")
    title = models.CharField("标题",max_length=255)
    statement = models.TextField("导语")
    time = models.IntegerField("发布时间")
    star = models.IntegerField("点赞数")
    tip_off = models.IntegerField("举报数")
    status = models.BooleanField("已发布/待审核",default=True)
    isPostByEditor=models.BooleanField("是否是编辑发布的内容",default=False)
    lastUpDateTime=models.IntegerField("话题最后更新时间")
    Fcounts=models.IntegerField("关注数",default=0)
    Tag=models.CharField("标签",max_length=255,default='')
    AgeRange_avg=models.IntegerField("受欢迎年龄段",default=0)
    hotPoints=models.FloatField("热门指数",default=0.0)

class Revelation(models.Model):

    class Meta:
        db_table = 'Revelation'
        verbose_name = '爆料'
        verbose_name_plural = '爆料'

    RID = models.AutoField("爆料ID", primary_key=True)
    TID=models.IntegerField("所属话题ID")
    UID=models.IntegerField("发布者ID")
    time=models.IntegerField("发布时间")
    title = models.CharField("标题", max_length=255)
    statement=models.TextField("导语")
    star=models.IntegerField("点赞数",default=0)
    tip_off=models.IntegerField("举报数",default=0)
    status = models.BooleanField("已发布/待审核", default=True)
    isPostByEditor = models.BooleanField("是否是编辑发布的内容", default=False)
    text=models.TextField("爆料内容")
    eventTime=models.DateTimeField("事件的时间节点")


class Revelation_Pic(models.Model):
    class Meta:
        db_table = 'Revelation_Pic'
        verbose_name = '爆料图片'
        verbose_name_plural = '爆料图片'

    RID=models.IntegerField("所属报料ID")
    img=models.ImageField("爆料图片",upload_to='baoliao',default='/static/img/default.png')


class Events(models.Model):
    class Meta:
        db_table = 'Events'
        verbose_name = '引用'
        verbose_name_plural = '引用'

    EID = models.AutoField("结点ID", primary_key=True)
    TID=models.IntegerField("所属话题ID")
    UID=models.IntegerField("发布者ID")
    time=models.IntegerField("发布时间")
    title = models.CharField("标题", max_length=255)
    statement=models.TextField("导语")
    star=models.IntegerField("点赞数")
    tip_off=models.IntegerField("举报数")
    status = models.BooleanField("已发布/待审核", default=True)
    isPostByEditor = models.BooleanField("是否是编辑发布的内容", default=False)
    url=models.CharField("来源URL",max_length=255)
    eventTime=models.DateTimeField("事件的时间节点")


class index_pic(models.Model):
    class Meta:
        db_table = 'index_pic'
        verbose_name = '首页图'
        verbose_name_plural = '首页图'

    PID=models.IntegerField("所属话题ID")
    img = models.ImageField("图片url", upload_to='index', default='/static/img/default.png')

class topic_vote(models.Model):
    class Meta:
        db_table = 'topic_vote'
        verbose_name = '话题投票'
        verbose_name_plural = '话题投票'

    TID = models.IntegerField("话题ID")
    ID = models.AutoField("选项ID", primary_key=True)
    item = models.CharField("条目名", max_length=255)
    counts = models.IntegerField("计数",default=0)


class activity(models.Model):
    class Meta:
        db_table = 'activity'
        verbose_name = '活动'
        verbose_name_plural = '活动'
    AID=models.AutoField("活动ID",primary_key=True)
    Title=models.TextField("活动标题")
    Introduction=models.TextField("活动介绍")
    isEND=models.BooleanField("正在进行/结束",default=False)
    reward=models.IntegerField("活动EXP奖励",default=0)
    poster = models.ImageField("活动海报", upload_to='poster', default='/static/img/default.png')


class activity_vote(models.Model):
    class Meta:
        db_table = 'activity_vote'
        verbose_name = '活动投票'
        verbose_name_plural = '活动投票'
    AID=models.IntegerField("活动ID")
    ID=models.AutoField("选项ID",primary_key=True)
    item=models.CharField("条目名",max_length=255)
    counts=models.IntegerField("计数")


class activity_contribute(models.Model):
    class Meta:
        db_table = 'activity_contribute'
        verbose_name = '活动投稿'
        verbose_name_plural = '活动投稿'

    A_CID = models.AutoField("投稿ID", primary_key=True)
    AID = models.IntegerField("所属活动ID")
    UID = models.IntegerField("发布者ID")
    time = models.IntegerField("发布时间")
    title = models.CharField("标题", max_length=255)
    statement = models.TextField("导语")
    star = models.IntegerField("点赞数", default=0)
    tip_off = models.IntegerField("举报数", default=0)
    status = models.BooleanField("已发布/待审核", default=True)
    text = models.TextField("投稿文字内容")
    hotPoints=models.FloatField("热值",default=0.0)

class contributes_Pic(models.Model):
    class Meta:
        db_table = 'contributes_Pic'
        verbose_name = '活动投稿图片'
        verbose_name_plural = '活动投稿图片'

    A_CID=models.IntegerField("所属活动投稿ID")
    img=models.ImageField("活动投稿图片",upload_to='tougao',default='/static/img/default.png')

class message(models.Model):
    class Meta:
        db_table = 'message'
        verbose_name = '消息'
        verbose_name_plural = '消息'
    UID=models.IntegerField("目标用户ID")
    type=models.IntegerField("类型")
    value=models.CharField("标题",max_length=255)
    postTime=models.DateTimeField("推送时间")

class Tip_off(models.Model):
    class Meta:
        db_table = 'tip_off'
        verbose_name = '举报审核队列'
        verbose_name_plural = '举报审核队列'

    type=models.IntegerField("对象类型")
    points=models.IntegerField("扣分数")
    UID=models.IntegerField("被举报人ID")
    valueID=models.IntegerField("举报对象ID",default=0)

class Star(models.Model):
    class Meta:
        db_table = 'Star'
        verbose_name = '点赞记录'
        verbose_name_plural = '点赞记录'

    type = models.IntegerField("对象类型")
    UID = models.IntegerField("点赞人ID")
    valueID = models.IntegerField("点赞对象ID")