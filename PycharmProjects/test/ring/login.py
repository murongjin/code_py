#!/usr/bin/env python3#coding=utf-8__auth__='Aaron'__date__='2018-04-10'#user list user_name:user_passworduser={'Aaron':'1','tom':'2','jim':'123456'}def login_name(func):    def ww(name,password):        if name in user:            print('*'*20)            print('name is ok')            func(name,password)            print('*'*20)        else:            print('name is error')    return wwdef login_password(func):    def ww(name,password):        if password == user[name]:            print('password is ok')            func(name,password)        else:            print('password is error')    return ww@login_name@login_passworddef login(name,password):    print("I'm %s ,my password is %s"%(name,password))login('tom','2')