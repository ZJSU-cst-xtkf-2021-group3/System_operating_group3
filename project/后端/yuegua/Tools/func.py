import time


host="http://101.37.175.115"

def ageSwitch(age):
    if age>=0 and age<=13:
        return 1
    if age>=14 and age<=17:
        return 2
    if age>=18 and age<=25:
        return 3
    if age >= 26 and age <= 35:
        return 4
    if age >= 36 and age <= 45:
        return 5
    if age >= 46 and age <= 56:
        return 6
    if age>=57:
        return 7

def exp2rank(exp):
    # lv1: 0 - 100
    # lv2: 101 - 300
    # lv3: 301 - 600
    # lv4: 601 - 1000
    # lv5: 1001 - 2000
    # lv6: 2001

    if 0<=exp and exp<=100:
        return 1
    if exp>=101 and exp<=300:
        return 2
    if exp>=301 and exp<=600:
        return 3
    if exp>=601 and exp<=1000:
        return 4
    if exp>=1001 and exp<=2000:
        return 5
    if exp>=2001:
        return 6

def check_right(rank):
    if rank<=3:
        return 'basic'
    if rank>=4:
        return 'full'


def getTime():
    return int(time.time())

def addEXP(uid,exp):
    from models.models import User
    usr=User.objects.get(UID__exact=uid)
    usr.EXP+=exp
    usr.save()
    if usr.ifPassedExam==False and usr.EXP>=601 :
        usr.rank=3
    else:
        usr.rank=exp2rank(usr.EXP)
    usr.save()

def stamp2strtime(stamp):
    return time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime(stamp))


# def img2base64(url:str):
#     with open(str(Set.BASE_DIR)+url, 'rb') as f:
#         code2=base64.b64encode(f.read())
#         print(code2)
#     return code2
#
def switchType(index):

    if index==1:
        return "话题"
    if index==2:
        return "引用"
    if index==3:
        return "爆料"
    if index==4:
        return "评论"
    if index==5:
        return "活动投稿"
