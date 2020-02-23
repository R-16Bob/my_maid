# my_maid by R-16Bob
import time
import random
import sys

#  提供可爱的不同时间的问候
def lovely_maid(): 
    print ("现在是:",localtime.tm_year,'年',localtime.tm_mon,'月',localtime.tm_mday,'日',localtime.tm_hour,'时',localtime.tm_min,'分')
    week()
    print('='*30,'\n主人，欢迎回来！(｡･∀･)ﾉﾞ')
    hour = localtime.tm_hour
    if(0<=hour<=4 or 23<=hour<=24):
        print('主人，夜深了，您还不睡吗？\n请您今天早点休息吧。要我陪您睡也是可以的哦(*/ω＼*)')
        print('我在说什么啊~~o(*////▽////*)q(脸红)')
    elif(5<=hour<=11):
        print('主人，早上好！ο(=•ω＜=)ρ⌒☆\n新的一天也要加油哦！')
    elif(12<=hour<=14):
        print('主人，中午的时光真是愉快呢，要来一杯咖啡吗？♪(´▽｀)')
    elif(15<=hour<=19):
        print('主人，下午的时间用来学习也不错呢\n学累了就睡我膝上吧(/ω＼*)(脸红)')
    else:
        print('主人辛苦一天了，现在可以休息一下哦o(^▽^)o')

#  使用算法告诉计算现在是第几周
def week():
    #  如何判定当前周数？
    d = {2:29,3:31,4:30,5:31,6:30,7:31}
    mon  = localtime.tm_mon
    day = localtime.tm_mday
    # mon = int(input('mon:')) 测试
    # day = int(input('day:'))
    i = mon
    num = 0  # 存储与2.24之差
    while(i>=2):
        if(mon==2):
            num += day-24
        elif(i==mon):
            num += day
        else:
            num += d[i]
        i -=1

    print('现在是大二第二学期的第',int(num/7+1),'周哦')

#  伪人工智能的聊天功能,可以随意调教
def chat():
    print('\n主人，我爱你！q(≧▽≦q)')
    str=''
    while 1:
        str = input('>')
        if(str == '我也爱你'):
            print('ヾ(≧▽≦*)o')
        elif(str == '再见' or str =='bye'):
            print('主人不要人家了吗 o(TヘTo)\n人家会一直等你哦')
            input()
            sys.exit()
        elif(str == '谢谢'):
            print('主人的开心就是人家的幸福哦 (´▽`ʃ♡ƪ)')
        elif(str=='不聊了'):
            print('好哒，主人')
            break
        else:
            print(str)

# 提供可更新的土味情话
def lovey_chat():
    d_love={0:('你上辈子一定是碳酸饮料吧','不然为什么我一看到你就能开心的冒泡'),
    1:('你知道你和星星有什么区别吗?','星星在天上，你在我心里'),
    2:('先生你要点什么?','我想点开你的心'),
    3:('你累不累啊?','可是你都在我脑里跑了一天了'),
    4:('你知道我的缺点是什么吗','是缺点你'),
    5:('我背你好吗?','因为你是我一辈子的人'),
    6:('你知道你和猴子的区别是什么吗? ','猴子住在树上，你住在我心里'),
    7:('有件事我怕我说漏了嘴',' 我爱你这件事。'),
    8:('你知道为什么我不上天吗','因为地上有你啊'),
    9:('为什么我那么笨','因为就长了这么点脑子都用来想你了。'),
    10:('我要早点睡觉了','明天还要继续喜欢你呢。'),
    11:('最近开始冷了','需要躲进你怀里的那种。')
    }
    
    s = '是'
    while(s!='no'and s!='不' and s!='不用了'and s!='n'):
        i = random.randrange(0,len(d_love))
        print(d_love[i][0])
        input('>')
        print(d_love[i][1])
        input('>')
        print('\n主人，要再来一个吗？')
        s = input('>')

#  非常常见的功能菜单
def menu():
    while 1:
        s = input('主人，要来聊天吗？~\(≧▽≦)/~(兴奋)\n>')
        if(s=='好啊'or s=='好' or s=='来聊天吧' or s=='y' or s=='yes'):
            chat()
        elif(s=='bye' or s=='再见'):
            print('主人我会想你的o(TヘTo)')
            input('')
            sys.exit()
        elif(s=='重启'or s=='restart' or s=='re'):
            print('系统开始重启')
            break
        else: 
            lovey_chat()
            print('主人，开心点了吗?( •̀ ω •́ )✧')
            input('>')
            print('您开心就好了呢')
        
    

    
while 1:
    localtime = time.localtime(time.time())
    lovely_maid()
    menu()
    input()
