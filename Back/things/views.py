from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

# 导入 activity 对象定义
from things.models import Things





def listthings(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Things.objects.values()

    ph = request.GET.get('tag', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(tag=ph)

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


