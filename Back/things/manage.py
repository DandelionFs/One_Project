from django.http import JsonResponse
import json
from things.models import Things

def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式,将json格式字符数变为Python对象
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']

    if action == 'list_thing':
        return listthing(request)
    elif action == 'add_thing':
        return addthing(request)
    elif action == 'modify_thing':
        return modifything(request)
    elif action == 'del_thing':
        return deletething(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listthing(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Things.objects.values()
    thingid = request.params['id']
    qs = qs.filter(id=thingid)

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)
    return JsonResponse({'retthing': 0, 'retlist': retlist})


def addthing(request):
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Things.objects.create(name=info['name'],
                                     date=info['date'],
                                     deadline=info['deadline'],
                                     time=info['time'],
                                     remind=info['remind'],
                                     tag=info['tag'],
                                     note=info['note'],

                                     )

    return JsonResponse({'ret': 0, 'id': record.id})


def modifything(request):
    # 从请求消息中 获取修改物品的信息
    # 找到该物品，并且进行修改操作

    thingid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        thing = Things.objects.get(id=thingid)
    except Things.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{thing}`的物品不存在'
        }

    if 'name' in newdata:
        thing.name = newdata['name']
    if 'date' in newdata:
        thing.date = newdata['date']
    if 'deadline' in newdata:
        thing.deadline = newdata['deadline']
    if 'time' in newdata:
        thing.time = newdata['time']
    if 'remind' in newdata:
        thing.remind = newdata['remind']
    if 'tag' in newdata:
        thing.tag = newdata['tag']
    if 'note' in newdata:
        thing.note = newdata['note']


    # 执行save才能将修改信息保存到数据库
    thing.save()

    return JsonResponse({'ret': 0})


def deletething (request):

    thingid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的物品记录
        thing = Things.objects.get(id=thingid)
    except Things.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{thing}`的物品不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    thing .delete()

    return JsonResponse({'ret': 0})
