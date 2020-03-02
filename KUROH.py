#这里是KURO的头文件库#

import tensorflow as tf
import numpy as np
import random
import math
import urllib.request
import urllib.parse
import urllib
import requests
import re
import json
import os,shutil
import time
import pandas as pd

def MoveFile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print (srcfile ,'not exist!')
    else:
        fpaths,fnames=os.path.split(srcfile)
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print ('move',srcfile,'->',dstfile)
        return fnames
#文件移动函数#

def CopyFile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print (srcfile ,'not exist!')
    else:
        fpaths,fnames=os.path.split(srcfile)
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print ('copy',srcfile,'->',dstfile)
        return fnames
#文件复制函数#

def Lock():
    i=0
    while(i<3):
        password = input('Please Enter The Password: ')
        key = int(password)
        if key==314159:
            break
        else:
            print('Please Try Again \n')
        i+=1
    if i<3:
        Authority=1
    else:
        Authority=0
    return Authority
#解锁函数，未来会升级成安全中心#

def Translate():
    while(1):
        c=input('What Do You Want To Translate :')
        data={}
        data['i']=c
        data['type']= 'AUTO'
        data['doctype']= 'json'
        data['version']: '2.1'
        data['keyfrom']= 'fanyi.web'
        data['ue']: 'UTF-8'
        data['typeresult']='ture'

        data=urllib.parse.urlencode(data).encode('utf-8')
        url='http://fanyi.youdao.com/translate'

        response=urllib.request.urlopen(url,data)
        html=response.read()

        target=json.loads(html)

        print('Reslut：%s'%(target['translateResult'][0][0]['tgt']))
        Exit = input('Do You Want Quit Tanslate[y/n]:')
        if Exit=='y':
            break
        elif Exit=='n':
            pass
        else:
            print('Please InPut The Right Letter ')
            time.sleep(2)
            break
#翻译函数#

def NeuralNetwork():
    Layers = 2
    NeuralNum = 10
    Epochs = 1000
    InShape = 1
    OutShape = 1
    Path,Layers,NeuralNum,InShape,OutShape,Epochs,Predict= g.multenterbox('Please Enter The Info Of Your NeuralNetWork ','NeuralNetWork',('Path','Layers','NeuralNum','InShape','OutShape','Epochs','Predict'))
    Predict = eval(Predict)
    Layers = int (Layers)
    NeuralNum = int (NeuralNum)
    InShape = int (InShape)
    OutShape = int (OutShape)
    Epochs = int (Epochs)
    data = pd.read_csv(Path)
    x = data.iloc[:,1:-1]
    y = data.iloc[:,-1]
    mod = tf.keras.Sequential(tf.keras.layers.Dense(NeuralNum, input_shape=(InShape,),activation='relu'))
    for i in range(0,Layers):
        mod.add(tf.keras.layers.Dense(NeuralNum))
    mod.add(tf.keras.layers.Dense(OutShape))
    mod.compile(optimizer='adam',loss='mse')
    history = mod.fit(x,y,epochs=Epochs)
    loss = history.history.get('loss')
#神经网络函数#

def Weather():
    url = 'http://tianqi.moji.com/weather/china/sichuan/chengdu'
    rsp = urllib.request.urlopen(url)
    html = rsp.read()
    html = html.decode()
    Weather =  re.findall(r'<meta name="description" content="(.*?)白天',html)[0]
    return Weather
#获取天气函数


def ShutDown():
    pass
#关闭函数,未来带数据保存#

