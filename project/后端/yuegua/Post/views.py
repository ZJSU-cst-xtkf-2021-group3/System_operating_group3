import json

from django.http import HttpResponse,HttpResponseRedirect
from models.models import User
from django.urls import reverse
from django.http import JsonResponse
from models.models import Topic
from models.models import Comments
from models.models import Events
from models.models import Revelation
from models.models import Revelation_Pic
from models.models import activity
from models.models import activity_contribute,userFollow_topic,userFollow_user
from models.models import contributes_Pic,topic_vote,activity_vote,message
from Tools import func as tools
from django.core.cache import cache

def post_topic(request):
    global pic
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')
    usr = User.objects.get(UID__exact=uid)

    if request.method=="POST":
        category=int(request.POST.get('category'))
        title=request.POST.get('title')
        statement=request.POST.get('statement')
        tag=request.POST.get('tag')

        try:
            pic = request.FILES.get('mainPic')
        except Exception as e:
            print(e)
        if not pic:
            pic='default.png'

        #用户等级权限判断
        if tools.check_right(usr.rank)!='full':
            result['res']='permission denied'
            return JsonResponse(result)

        #用户经验值更新
        usr.EXP+=15
        #用户等级更新
        usr.rank=tools.exp2rank(usr.EXP)
        usr.save()
        tmpTime=tools.getTime()

        try:
            t=Topic.objects.create(UID=usr.UID,category=category,title=title,statement=statement,Tag=tag,
                             time=tmpTime,star=0,tip_off=0,status=True,isPostByEditor=False,
                             Fcounts=0,lastUpDateTime=tmpTime,hotPoints=usr.rank*5,mainPic=pic)
            #审核消息
            message.objects.create(UID=usr.UID,type=1,typeID=t.TID,value="您的"+tools.switchType(1)+"稿件已审核通过",postTime=tools.getTime())
            #即时消息
            ftlist=userFollow_topic.objects.filter(FTID__exact=t.TID)
            for fu in ftlist:
                token = str(fu.UID) + 'Ftopic'
                cache.set(token, "您关注的"+t.title+"话题更新啦！", 21)

            fblist = userFollow_user.objects.filter(FUID__exact=usr.UID)
            for fu in fblist:
                token = str(fu.UID) + 'Fbot'
                cache.set(token, "博主" + fu.FUname + "发布了新内容，快去看看吧", 21)


        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)
        
        result['res']='ok'
        return JsonResponse(result)

def post_comment(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')


    if request.method=='POST':

        try:
            u = User.objects.get(UID__exact=uid)
            TID = int(request.POST.get('TID'))
            value = request.POST.get('value')
            Comments.objects.create(UID=uid,TID=TID,value=value,time=tools.getTime(),star=0,status=True,tip_off=0,
                                   hotPoints=u.rank*5)
            # 用户经验值更新
            tools.addEXP(u.UID,4)

            #即时通知
            fblist = userFollow_user.objects.filter(FUID__exact=u.UID)
            for fu in fblist:
                token = str(fu.UID) + 'Fbot'
                cache.set(token, "博主" + fu.FUname + "发布了新内容，快去看看吧", 21)

            t=Topic.objects.get(TID__exact=TID)
            cache.set(str(t.UID)+"Ncomment","您的"+t.title+"话题收到了回复",21)

        except Exception as e:
            print(e)
            result['res']='failed'
            return JsonResponse(result)

        result['res']='ok'
        return JsonResponse(result)

def post_event(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid=request.POST.get('uid')

    #权限检查
    usr=User.objects.get(UID__exact=uid)
    if usr.ifPassedExam==False:
        result['res']='permission denied'
        return JsonResponse(result)

    if request.method=='POST':
        tid=int(request.POST.get('TID'))
        title=request.POST.get('title')
        statement=request.POST.get('statement')
        url=request.POST.get('url')
        eventTime=request.POST.get('eventTime')

        try:
            #更新话题最后更新时间
            tmpTime=tools.getTime()
            topic=Topic.objects.get(TID__exact=tid)
            topic.lastUpDateTime=tmpTime
            topic.save()

            e=Events.objects.create(TID=tid,UID=uid,time=tmpTime,title=title,statement=statement
                                  ,star=0,tip_off=0,status=True,isPostByEditor=False,url=url,eventTime=eventTime)
            message.objects.create(UID=usr.UID, type=2, typeID=e.EID, value="您发布的" + tools.switchType(2) + "内容已审核通过啦！",postTime=tools.getTime())
            #exp
            tools.addEXP(uid,10)

            #即时通知
            fblist = userFollow_user.objects.filter(FUID__exact=usr.UID)
            for fu in fblist:
                token = str(fu.UID) + 'Fbot'
                cache.set(token, "博主" + fu.FUname + "发布了新内容，快去看看吧", 21)

            cache.set(str(topic.UID) + "Nevent", "您的" +topic.title+ "话题有新的结点", 21)

        except Exception as e :
            print(e)
            result['res']='failed'
            return JsonResponse(result)

        result['res'] = 'ok'
        return JsonResponse(result)

def post_revelation(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = request.POST.get('uid')

    # 权限检查
    usr = User.objects.get(UID__exact=uid)
    if usr.ifPassedExam == False:
        result['res'] = 'permission denied'
        return JsonResponse(result)

    if request.method == 'POST':
        tid = int(request.POST.get('TID'))
        title = request.POST.get('title')
        statement = request.POST.get('statement')
        eventTime = request.POST.get('eventTime')
        text=request.POST.get('text')


        try:
            # 更新话题最后更新时间
            tmpTime = tools.getTime()
            topic = Topic.objects.get(TID__exact=tid)
            topic.lastUpDateTime = tmpTime
            topic.save()

            R=Revelation.objects.create(TID=tid, UID=uid, time=tmpTime, title=title, statement=statement
                                  , star=0, tip_off=0, status=True, isPostByEditor=False, eventTime=eventTime,text=text)

            #通知
            message.objects.create(UID=uid, type=3, typeID=R.RID, value="您的" + tools.switchType(3) + "稿件已审核通过!",postTime=tools.getTime())
            fblist = userFollow_user.objects.filter(FUID__exact=usr.UID)
            for fu in fblist:
                token = str(fu.UID) + 'Fbot'
                cache.set(token, "博主" + fu.FUname + "发布了新内容，快去看看吧", 21)

            cache.set(str(topic.UID) + "Nevent", "您的" + topic.title + "话题有新的结点", 21)

            picsUPload = request.FILES.getlist('imgs')
            try:
                for f in picsUPload:
                    Revelation_Pic.objects.create(RID=R.RID,img=f)
            except Exception as e1:
                print(e1)
                result['res'] = 'failed'
                return JsonResponse(result)
            # exp
            tools.addEXP(uid, 10)

        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)

        result['res'] = 'ok'
        return JsonResponse(result)

def post_Activity(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = request.POST.get('uid')

    # 权限检查
    usr = User.objects.get(UID__exact=uid)
    if usr.isEDIT == False:
        result['res'] = 'permission denied'
        return JsonResponse(result)

    if request.method=='POST':
        title=request.POST.get('title')
        introduction=request.POST.get('introduction')
        reward=int(request.POST.get('reward'))
        poster = request.FILES.get('poster')

        try:
            activity.objects.create(reward=reward,poster=poster,Introduction=introduction,Title=title,isEND=False,hotPoints=usr.rank*5)
        except Exception as e:
            print(e)
            result['res']='failed'
            return JsonResponse(result)

        result['res']='ok'
        return JsonResponse(result)


def post_activity_contribute(request):
    result = {
        'res': ''
    }
    uid = int(request.session.get('uid', '-1'))
    if uid == -1:
        result['res'] = 'login please'
        return JsonResponse(result)
    # uid = int(request.POST.get('uid'))


    if request.method == 'POST':
        aid = int(request.POST.get('AID'))
        title = request.POST.get('title')
        statement = request.POST.get('statement')
        text = request.POST.get('text')

        try:
            u = User.objects.get(UID__exact=uid)
            ac = activity_contribute.objects.create(AID=aid, UID=uid, time=tools.getTime(), title=title, statement=statement
                                          , star=0, tip_off=0, status=True, text=text,hotPoints=u.rank*5)

            #通知
            message.objects.create(UID=uid, type=5, typeID=ac.A_CID, value="您的" + tools.switchType(5) + "已通过审核",postTime=tools.getTime())
            fblist = userFollow_user.objects.filter(FUID__exact=uid)
            for fu in fblist:
                token = str(fu.UID) + 'Fbot'
                cache.set(token, "博主" + fu.FUname + "发布了新内容，快去看看吧", 21)

            picsUPload = request.FILES.getlist('imgs')
            try:
                for f in picsUPload:
                    contributes_Pic.objects.create(A_CID=ac.A_CID,img=f)
            except Exception as e1:
                print(e1)
                result['res'] = 'failed'
                return JsonResponse(result)
            # exp
            a=activity.objects.get(AID__exact=aid)
            tools.addEXP(uid, a.reward)


        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)

        result['res'] = 'ok'
        return JsonResponse(result)

def Topic_vote(request):
    result = {
        'res': ''
    }
    if request.method=='POST':
        msg=json.loads(request.body.decode())
        itemList=msg['items']
        tid=int(msg['TID'])
        try:
            for i in itemList:
                topic_vote.objects.create(TID=tid,item=i,counts=0)
        except Exception as e:
            print(e)
            result['res']='failed'
            return JsonResponse(result)

    result['res']='ok'
    return JsonResponse(result)

def Activity_vote(request):
    result = {
        'res': ''
    }
    if request.method == 'POST':
        msg = json.loads(request.body.decode())
        itemList = msg['items']
        aid = int(msg['AID'])
        try:
            for i in itemList:
                activity_vote.objects.create(AID=aid,item=i,counts=0)
        except Exception as e:
            print(e)
            result['res'] = 'failed'
            return JsonResponse(result)

    result['res'] = 'ok'
    return JsonResponse(result)