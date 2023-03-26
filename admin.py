# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:28:19 2022

@author: 陳永興
"""
# import getpass  # Prompt the user for a password without echoing.  Spyder console 不支援!
import sys  # 使用 exit() 終止程式執行

class Admin:
    def __init__(self, uid = 'lucas', pwd = '123456', pwd_hint = '7110029138'):  # 初始化管理員
        self.uid = uid  # uid: 帳號
        self.pwd = pwd  # pwd: 密碼
        self.pwd_hint = pwd_hint  # pwd_hint: 密碼提示
    def login(self):  # 登入方法
        chance = 3  # 連續輸入錯誤容忍總次數
        count = 0  # 已輸入錯誤次數
        while count < 3:
            uid = input('請輸入帳號: ')
            # pwd = getpass.getpass('請輸入密碼: ')
            pwd = input('請輸入密碼: ')
            if uid == self.uid and pwd == self.pwd:
                print('登入成功!')
                print('----------------')
                return True
            else:  # 連續輸入錯誤帳號或密碼超過特定次數
                print('----------------')
                print('帳號或密碼錯誤,請重新輸入!')
                print('連續輸入錯誤超過3次，系統將強制終止!')
                chance -= 1
                print('您還剩下 %d 次機會!' % chance)
                print('----------------')
                count += 1
        print('See you soon!')
        sys.exit(0)
    
    def query_pwd(self):  # 忘記密碼方法
        chance = 3  # 連續輸入錯誤容忍總次數
        count = 0  # 已輸入錯誤次數
        print('**** 忘記密碼 ****')
        while count < 3:
            q_pwd = input('請輸入學號進行身分驗證: ')
            # q_pwd = getpass.getpass('請輸入學號進行身分驗證: ')
            if q_pwd == self.pwd_hint:
                print('帳號 %s 的密碼是 %s' % (self.uid, self.pwd))
                print('----------------')
                return True
            else:
                # 連續輸入錯誤帳號或密碼超過特定次數
                print('----------------')
                print('身分驗證錯誤,請重新輸入!')
                print('連續輸入錯誤超過3次，系統將強制終止!')
                chance -= 1
                print('您還剩下 %d 次機會!' % chance)
                print('----------------')
                count += 1
        print('See you soon!')
        sys.exit(0)