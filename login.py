import requests
import json
import random
import time
from acfunMoile import FileController as FC

requests.packages.urllib3.disable_warnings()


def login(username, password):
    url = "https://id.app.acfun.cn/rest/app/login/signin?app_version=6.27.1.984&market=baidusem07&sys_name=android" \
          "&appMode=0&socName=UNKNOWN&boardPlatform=gmin&sys_version=5.1.1&product=ACFUN_APP "
    data = {
        "username": username,
        "password": password
    }
    header = {

        "Accept-Encoding": "gzip, deflate, br",
        "User-agent": "acvideo core/6.27.1.984(OnePlus;HD1910;5.1.1) aegon/1.18.0-curl",
        "Content-Type": "application/x-www-form-urlencoded",
        "deviceType": "1",
        "acPlatform": "ANDROID_PHONE",
        "appVersion": "6.27.1.984",
        "gid": "DFP26874595120E975B974E18D75B503461D0A5B79E8CD5339009C1017A9F6A5",
        "isChildPattern": "false",
        "isp": "CMCC",
        "language": "zh-cn",
        "market": "baidusem07",
        "mod": "OnePlus(HD1910)",
        "net": "WIFI",
        "productId": "2000",
        "random": "28809836-9e30-481e-8997-e98908996643",
        "requestTime": "2020-08-03 01:23: 48.769",
        "resolution": "720x1280",
        "sign": "2196437839c9a49235d27791089411af794ce6d3fe",
        "udid": "4161d10b-c0c9-36c0 -a771-47139def3533",
        "url_page": "LOGIN",
        "uuid": "4d14ecca - f04a - 404c - ae72 - 870e8302c7d0",
        "token": ""
    }
    session = requests.Session()
    response = session.post(url, headers=header, data=data, verify=False)
    ck_dict = json.loads(response.text)
    FC.save("tokendict.txt", ck_dict)
    ck_jar = requests.utils.cookiejar_from_dict(ck_dict)
    ck_str = ""
    ck_str = ck_str + "acPasstoken" + "=" + str(ck_jar["acPassToken"]) + ";"
    ck_str = ck_str + "auth_key" + "=" + str(ck_jar["auth_key"]) + ";"
    ck_str = ck_str + "old_token" + "=" + str(ck_jar["token"]) + ";"
    ck_str = ck_str + "userId" + "=" + str(ck_jar["userid"]) + ";"
    ck_str = ck_str + "acfun.midground.api_st" + "=" + "ChZhY2Z1bi5taWRncm91bmQuYXBpLnN0EmBDsa7OeafT4" \
                                                       "-brdSlbqoyVVZImB8IeDWY3G0Qa-nWWbajIxFQpn4WIEIuRzFQHAuL2dR1CRa" \
                                                       "-EjWZctQsw-ibjpNbDzFqzlEJt7gwxqVBRZE" \
                                                       "-qDUMksZxkEoyDgV2GDrMaErVcnpVLEuvQ4UZ4dHm4FLjsrSIgI8UgnEATCJuLTf8Ts3obAmbenq05bHktux7OYB0VRbooBTAB;"
    FC.save("token.txt", ck_str)
    return ck_str


def getPersionInfo(ck_str):
    url = "https://api-new.app.acfun.cn/rest/app/user/personalInfo?app_version=6.27.1.984&market=baidusem07&sys_name" \
          "=android&appMode=0&socName" \
          "=UNKNOWN&boardPlatform=gmin&sys_version=5.1.1&product=ACFUN_APP "
    header = {"Accept-Encoding": "gzip, deflate, br",
              "User-agent": "acvideo core/6.27.1.984(OnePlus;HD1910;5.1.1) aegon/1.18.0-curl",
              "Content-Type": "application/json; charset=UTF-8", "deviceType": "1", "acPlatform": "ANDROID_PHONE",
              "appVersion": "6.27.1.984", "isChildPattern": "false", "isp": "CMCC", "language": "zh-cn",
              "market": "baidusem07", "mod": "OnePlus(HD1910)", "net": "WIFI", "productId": "2000",
              "random": "28809836-9e30-481e-8997-e98908996643", "requestTime": "2020-08-03 01:23: 48.769",
              "resolution": "720x1280", "sign": "2196437839c9a49235d27791089411af794ce6d3fe",
              "udid": "4161d10b-c0c9-36c0 -a771-47139def3533", "url_page": "PROFILE",
              "uuid": "08abbae5-94f5-46b5-8015-b7120e79ec73", "Cookie": ck_str}
    # header["uid"]=str(ck_jar["userid"])
    # header["access_token"]=ck_jar["token"]
    response = requests.get(url, headers=header, verify=False)
    print(response.text)
    response_jar = json.loads(str(response.text))
    print(response_jar["info"])
    return response_jar["info"]


def artical_list(ck_str, search_str: str, p=0):
    url = "https://api-new.app.acfun.cn/rest/app/search/article?" \
          "app_version=6.27.1.984" \
          "&market=baidusem07" \
          "&sys_name=android&appMode=0" \
          "&socName=UNKNOWN&boardPlatform=gmin" \
          "&sys_version=5.1.1" \
          "&product=ACFUN_APP " \
          "&keyword=" + search_str + ";" \
                                     "&requestId=;" \
                                     "&Cursor=" + str(p) + ";" \
                                                           "sortType=5;"
    header = {"Accept-Encoding": "gzip, deflate, br",
              "User-agent": "acvideo core/6.27.1.984(OnePlus;HD1910;5.1.1) aegon/1.18.0-curl",
              "Content-Type": "application/json; charset=UTF-8", "deviceType": "1", "acPlatform": "ANDROID_PHONE",
              "appVersion": "6.27.1.984", "isChildPattern": "false", "isp": "CMCC", "language": "zh-cn",
              "market": "baidusem07", "mod": "OnePlus(HD1910)", "net": "WIFI", "productId": "2000",
              "random": "28809836-9e30-481e-8997-e98908996643", "requestTime": "2020-08-03 01:23: 48.769",
              "resolution": "720x1280", "sign": "2196437839c9a49235d27791089411af794ce6d3fe",
              "udid": "4161d10b-c0c9-36c0 -a771-47139def3533", "url_page": "PROFILE",
              "uuid": "08abbae5-94f5-46b5-8015-b7120e79ec73", "Cookie": ck_str}
    response = requests.get(url, headers=header, verify=False)
    print(response.text)
    response_jar = json.loads(response.text)
    print(response_jar["articleList"])
    itemList = response_jar["articleList"]
    return itemList


# 关注某人
def follow(ck_str, userid: str):
    url = "https://api-new.app.acfun.cn/rest/app/relation/follow?app_version=6.27.1.984&market=baidusem07&sys_name" \
          "=android&appMode=0&socName" \
          "=UNKNOWN&boardPlatform=gmin&sys_version=5.1.1&product=ACFUN_APP "
    data = {
        "action": "1",
        "groupId": "0",
        "toUserId": userid
    }
    header = {"Accept-Encoding": "gzip, deflate, br",
              "User-agent": "acvideo core/6.27.1.984(OnePlus;HD1910;5.1.1) aegon/1.18.0-curl",
              "Content-Type": "application/x-www-form-urlencoded", "deviceType": "1", "acPlatform": "ANDROID_PHONE",
              "appVersion": "6.27.1.984", "isChildPattern": "false", "isp": "CMCC", "language": "zh-cn",
              "market": "baidusem07", "mod": "OnePlus(HD1910)", "net": "WIFI", "productId": "2000",
              "random": "28809836-9e30-481e-8997-e98908996643", "requestTime": "2020-08-03 01:23: 48.769",
              "resolution": "720x1280", "sign": "2196437839c9a49235d27791089411af794ce6d3fe",
              "udid": "4161d10b-c0c9-36c0 -a771-47139def3533", "url_page": "PROFILE",
              "uuid": "08abbae5-94f5-46b5-8015-b7120e79ec73", "Cookie": ck_str}
    response = requests.post(url, headers=header, data=data, verify=False)
    response_dict = response.json()
    if response_dict["result"] == 0:
        print(response.json())
        print("关注用户UID:" + userid + "   成功")
        return 1
    else:
        print(response.json())
        print("关注失败")


# 转发动态
def add_moment(ck_str, articleid: str):
    url = "https://api-new.app.acfun.cn/rest/app/moment/add?app_version=6.27.1.984&market=baidusem07&sys_name" \
          "=android&appMode=0&socName" \
          "=UNKNOWN&boardPlatform=gmin&sys_version=5.1.1&product=ACFUN_APP"
    data = {
        "params": "{\"content\":\"\",\"repostResourceId\":"+articleid+",\"repostResourceType\":3}"
    }
    header = {"Accept-Encoding": "gzip, deflate, br",
              "User-agent": "acvideo core/6.27.1.984(OnePlus;HD1910;5.1.1) aegon/1.18.0-curl",
              "Content-Type": "application/x-www-form-urlencoded", "deviceType": "1", "acPlatform": "ANDROID_PHONE",
              "appVersion": "6.27.1.984", "isChildPattern": "false", "isp": "CMCC", "language": "zh-cn",
              "market": "baidusem07", "mod": "OnePlus(HD1910)", "net": "WIFI", "productId": "2000",
              "random": "28809836-9e30-481e-8997-e98908996643", "requestTime": "2020-08-03 01:23: 48.769",
              "resolution": "720x1280", "sign": "2196437839c9a49235d27791089411af794ce6d3fe",
              "udid": "4161d10b-c0c9-36c0 -a771-47139def3533", "url_page": "PROFILE",
              "uuid": "08abbae5-94f5-46b5-8015-b7120e79ec73", "Cookie": ck_str}
    response = requests.post(url, headers=header, data=data, verify=False)
    response_dict = response.json()
    if response_dict["result"] == 0:
        print("转发文章:" + articleid + "--成功")
        return 1
    else:
        print("转发失败")
        print(response.json())
        return 0


# 评论
def add_comment(ck_str, content: str, sourceId: str, token: str):
    url = "https://api-new.app.acfun.cn/rest/app/comment/add?app_version=6.27.1.984&market=baidusem07&sys_name" \
          "=android&appMode=0&socName" \
          "=UNKNOWN&boardPlatform=gmin&sys_version=5.1.1&product=ACFUN_APP"
    data = {
        "sourceId": sourceId,
        "sourceType": 1,
        "content": content,
        "syncToMoment": 0,
        "access_token": token
    }
    header = {"Accept-Encoding": "gzip, deflate, br",
              "User-agent": "acvideo core/6.27.1.984(OnePlus;HD1910;5.1.1) aegon/1.18.0-curl",
              "Content-Type": "application/x-www-form-urlencoded", "deviceType": "1", "acPlatform": "ANDROID_PHONE",
              "appVersion": "6.27.1.984", "isChildPattern": "false", "isp": "CMCC", "language": "zh-cn",
              "market": "baidusem07", "mod": "OnePlus(HD1910)", "net": "WIFI", "productId": "2000",
              "random": "28809836-9e30-481e-8997-e98908996643", "requestTime": "2020-08-03 01:23: 48.769",
              "resolution": "720x1280", "sign": "2196437839c9a49235d27791089411af794ce6d3fe",
              "udid": "4161d10b-c0c9-36c0 -a771-47139def3533", "url_page": "PROFILE",
              "uuid": "08abbae5-94f5-46b5-8015-b7120e79ec73", "Cookie": ck_str}
    response = requests.post(url, headers=header, data=data, verify=False)
    response_dict = response.json()
    if response_dict["result"] == 0:
        print("评论文章id:" + sourceId)
        print("评论内容: " + content)
        print("状态:成功")
        return 1
    else:
        print(response.json())
        print("评论失败")
        return 0


def test():
    # 第一次登陆需要用户名密码获取token
    # login("Your username","Your password")
    ck_str = FC.read("token.txt")
    ck_dict = FC.read_dict("tokendict.txt")
    art_list = artical_list(ck_str, "抽奖")
    hasfollow = FC.read_dict("hasfollow.txt")
    hasadd_moment = FC.read("hasadd_moment.txt")
    hasadd_comment = FC.read("hasadd_comment.txt")
    comment = ["我来组成分子", "我来组成分母", "让我当一回欧皇", "我不要做非酋了", "冲冲冲！！！", "弟弟来了", "非酋在此", "分母+1", "分子+1"]
    k = 0
    for item in art_list:
        print("文章标题:" + item["emTitle"])

        # 五秒一次
        flag = 1
        index = int(random.randint(0, len(comment))) % 9
        # 关注
        if item["userId"] not in hasfollow:
            flag = flag | follow(ck_str, str(item["userId"]))
            hasfollow[item["userId"]] = 1
        # 评论
        # if item["contentId"] not in hasadd_comment:
        #     flag = flag | add_comment(ck_str, comment[index], str(item["contentId"]), ck_dict["token"])
        #     hasadd_moment[item["contentId"]] = 1
        # 转发
        if item["contentId"] not in hasadd_moment:
            flag = flag | add_moment(ck_str, str(item["contentId"]))
            hasadd_comment[item["contentId"]] = 1
            hasadd_moment[item["contentId"]] = 1
        if flag == 1:
            print("----------------------评论转发关注成功-----------------")
        else:
            print("----------------------评论转发关注失败-----------------")
            break
        k+=1
        time.sleep(10)
        if k == 5:
            break

    FC.save("hasfollow.txt",hasfollow)
    FC.save("hasadd_comment.txt",hasadd_comment)
    FC.save("hasadd_moment.txt",hasadd_moment)
    # ck_dict = FC.read_dict("tokendict.txt")
    # print(type(ck_dict))
    # personInfo = getPersionInfo(ck_str)
    # FC.save("PersonInfo.txt",str(personInfo))
    # artical_list(ck_str,"抽奖",1)
    # follow(ck_str,"32123067")
    # add_moment(ck_str,"17197130")
    # add_commmet(ck_str,"拉低中奖率","17197130",ck_dict["token"])


test()
