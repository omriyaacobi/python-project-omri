# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def Dictt():
    dict={}
    value=''
    key=''
    i=0
    while i<3:
    
        
        
            
        key=input('plaese enter key')
        if key in dict.keys():
            print('the key you entered already exsists. please enter a new key')
            
            
        else:
            value=input('please enter value')
            if value.isdigit():
                x={key:value}
                dict.update(x)
                i=i+1
            else: 
                    print ('the value you entered is not an integer. enter a new value')
    
    return dict

def check(dict):
    x=input('enter key')
    if x in dict.keys():
        print ('yes')
        
    else: 
        print ('no')
def main():
    
    dict=Dictt()
    print (dict)
    y=check(dict)
    
    
    
    
    
if __name__ == "__main__":
    main()


