#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
# Time : 2021/4/23 21:30
# Author : Wuya
import json
from rest_framework.views import APIView
from aliyunsdkcore import client
from aliyunsdkafs.request.v20180112 import AuthenticateSigRequest
from aliyunsdkcore.profile import region_provider
from djangoblog.settings import AccessKeyID, AccessKeySecret
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response


region_provider.add_endpoint('afs', 'cn-hangzhou', 'afs.aliyuncs.com')


class Captcha(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = json.loads(request.POST.get("captcha_data"))

        clt = client.AcsClient(AccessKeyID, AccessKeySecret, 'cn-hangzhou')
        request = AuthenticateSigRequest.AuthenticateSigRequest()

        # 必填参数：从前端获取，不可更改，android和ios只传这个参数即可
        request.set_SessionId(data["sessionId"])
        # 必填参数：从前端获取，不可更改
        request.set_Sig(data["sig"])
        # 必填参数：从前端获取，不可更改
        request.set_Token(data["token"])
        # 必填参数：从前端获取，不可更改
        request.set_Scene(data["scene"])
        # 必填参数：后端填写
        request.set_AppKey('FFFF0N00000000009E4C')
        # 必填参数：后端填写
        request.set_RemoteIp('127.0.0.1:9999')

        result = clt.do_action(request)  # 返回code 100表示验签通过，900表示验签失败
        code = (str(result).split("<Code>")[1].split("</Code>")[0])
        return Response(code)
