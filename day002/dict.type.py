import json
#字典 以 {} 包起来  :前面位 key   后面为 value
adict = {"username":"admin","password":"123456"}
# 字典是无序的,他没有索引,只能通过 key 去访问 value 并且 key 不能重复

#查看
def dict1_sel():
    print (adict['username'])
#更改,key 不可更改   只能通过key 去更改 value
def dict2_update():
    adict['password'] = '果芽软件'
    print (adict)
def dict3_del():
    adict.pop('password')
    print (adict)
def dict4_add():
    #增加一个键值对
    adict['list'] = '321123'
    print (adict)
    #合并字典1 将bdict 加入adict
    bdict = {'zd1':'guoya','zd2':'果芽'}
    adict.update(bdict)
    print (adict)
    #合并字典2 将cdict 与 adict 合并 第二个字典前要加 **
    cdict = {'zzz':'1','zzz2':'2'}
    ddict = dict(adict, **cdict)
    print (ddict)
def dict5_json():
    #将字典 dict 更新为 字符串类型 str
    print (adict)
    json_str = json.dumps(adict,ensure_ascii=False)
    print (json_str)
    print (type(json_str))
    #将 字符串 str 更新为字典 dist
    edict = '{"username": "admin", "password": "123456"}'
    json_loads = json.loads(edict)
    print (json_loads)
    print (type(json_loads))


if __name__ == '__main__':
    dict1_sel()
    dict2_update()
    dict3_del()
    dict4_add()
    dict5_json()