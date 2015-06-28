# -*- coding:utf-8 -*-


def convertName(cityName):
    #将 “浙江省杭州市” 转换成“杭州”
    #print 'convertName:',cityName

    name=cityName
    print type(name)

    if name.find(u"省") !=-1:# 包含'省'
        #print u'有省'
        name=name.split(u'省')[1]
        
   
    
    if name.find(u"市") != -1:#包含‘市’
        #print u'有市'
        name=name.split(u'市')[0]
    if name.find(u"省") !=-1:
         name=name.split(u'江')[0]
    return name
   

cityName='浙江省'
u = cityName.decode("utf-8")

fun=convertName(u)
print fun
