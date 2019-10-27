# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:02:36 2019

@author: omri
"""

def Baribua():
    dict={}
    i=0
    key=''
    value=''
    while i<5:
       
        key=input('please enter number')
        if(key.isdigit()==False):
            print('you did not enter an integer. try again')
        else:
            x={key:int(key) * int(key)}
            dict.update(x)
            i=i+1
                
    return dict

def main():
    dict=Baribua()
    print (dict)



if __name__ == "__main__":
    main()