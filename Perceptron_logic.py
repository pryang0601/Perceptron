import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
import random

def Open(s):
    with open("/Users/pryang/Documents/類神經網路/HW1/fundamental/"+s,"r") as f:
        lines=f.readlines()
        X=[float(line.split()[0]) for line in lines]
        Y=[float(line.split()[1]) for line in lines]
        Z=[line.split()[2] for line in lines]
        train_X,test_X,train_Y,test_Y,train_Z,test_Z=train_test_split(X,Y,Z,test_size=0.34,random_state=42,stratify=Z)
        train_size=len(train_X)
        test_size=len(test_X)
        return ([X,Y,Z,train_X,test_X,train_Y,test_Y,train_Z,test_Z,train_size,test_size])
#function:
def Sign(w,i,MaxV,MinV):
    Wt=np.array(w)
    Xn=np.array(i)
    mul=np.matmul(Wt,Xn)
    if mul>=0:
        expect=MaxV
    else:
        expect=MinV
    return str(expect)

def Adjust(w,x,expect,r,MaxV,MinV):
    Wt=np.array(w)
    Xn=np.array(x)
    result=float(np.matmul(Wt,Xn))
    if expect==MaxV and result<0:
        w_new=Wt+r*Xn
    elif expect==MinV and result>=0:
        w_new=Wt-r*Xn
    else:
        w_new=Wt
    w_new=np.round(w_new,3)
    return list(w_new)

#main
def MainTrain(Z,train_X,train_Y,train_Z,train_size,rate,epo):
    w_init=[-1,random.random(),random.random()]                        #初始化鏈結值    
    MaxValue=int(max(Z))
    MinValue=int(min(Z))
    n=1
    train_equal=train_size
    #start training
    w=w_init
    stop_i=train_size
    texts=""
    stoptrain=False
    while n>0:
        errorh=False
        if n>epo or stoptrain==True:                     
            break
        train_equal=train_size
        for i in range(train_size):
            input_v=[-1,float(train_X[i]),float(train_Y[i])]
            output=Sign(w,input_v,MaxValue,MinValue)
            texts+=("("+str(float(train_X[i]))+","+str(float(train_Y[i]))+") 的訓練結果:"+str(output)+'\n')
            if output!=train_Z[i]:
                errorh=True
                stop_i=i
                train_equal-=1
                w=Adjust(w,input_v,int(train_Z[i]),rate,MaxValue,MinValue)
            if stop_i==i and errorh==False:
                stoptrain=True
                break
        if errorh==True:
            n+=1
    with open("Training.txt","w") as f:
        f.write(texts)
    return [w,train_equal]

def MainTest(test_size,test_X,test_Y,test_Z,MaxValue,MinValue,w):
    test_equal=test_size
    texts=""
    for i in range(test_size):
        test_input=[-1,float(test_X[i]),float(test_Y[i])]
        output=Sign(w,test_input,MaxValue,MinValue)
        texts+=("("+str(float(test_X[i]))+","+str(float(test_Y[i]))+") 的測試結果:"+str(output)+'\n')
        if output!=test_Z[i]:
            test_equal-=1
    with open("Testing.txt","w") as f:
        f.write(texts)
    return test_equal

def Plot(weight,X,Y,Z,MaxV):
    a=weight[0]
    b=weight[1]
    c=weight[2]
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    def pltcolor(V):
        color=[]
        for v in V:
            if v==MaxV:
                color.append('red')
            else:
                
                color.append('blue')
        return color
    cols=pltcolor(Z)
    ax.scatter(X,Y,c=cols,s=1)
    plotx=X
    ploty=[]
    for x in X:
        y=float(a/c)-float(b/c)*x
        ploty.append(y)
    plt.plot(plotx,ploty,'-g')
    plt.title("Perceptron")
    plt.xlabel("Dimension-1")
    plt.ylabel("Dimension-2")
    plt.savefig("Perceptron")
    #plt.show()