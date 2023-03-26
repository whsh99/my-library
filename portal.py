# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 19:26:04 2022

@author: 陳永興
"""
import sys  # 使用 exit() 終止程式執行
from admin import Admin  # 從 Admin 模組導入 Admin 類別
from funs import Books  # 從 Funs 模組導入 Books 類別

def main():
    while True:
        print('**** 首頁 ****')
        print('登入請輸入: 1')
        print('忘記密碼請輸入: 2')
        print('----------------')
        print('退出請按任意鍵...')
        print('----------------')
        func1 = input('')  # 輸入首頁功能編號
        admin = Admin()  # 定義 user 物件
        if func1 == '1':  # 登入
            legit = admin.login()  # legit: 是否成功登入
            if legit == True:
                book = Books()
                while True:
                    book.menu()
                    func2 = input('請選擇功能? ')
                    print('----------------')
                    if func2 == '0':  # 登出
                        print('See you soon!')
                        sys.exit(0)
                    if func2 == '1':  # 列出所有書籍
                        book.list_all()
                    if func2 == '2':  # 依類別查詢書籍
                        book.query_type()
                    if func2 == '3':  # 依書號查詢書籍
                        book.query_bn()
                    if func2 == '4':  # 新增書籍
                        book.add()
                    if func2 == '5':  # 刪除書籍
                        book.delete()
                    if func2 == '6':  # 修改書籍
                        book.revise()
                    if func2 != '1' and func2!= '2' and func2 != '3' and func2 != '4' and func2 != '5' and func2 != '6':  # 輸入未在範圍內的功能編號
                        print('請重新輸入!')
                        print('----------------')
        if func1 == '2':  # 忘記密碼
            admin.query_pwd()
        if func1 != '1' and func1 != '2':
            print('See you soon!')
            sys.exit(0)

if __name__ == '__main__':  # 避免執行其它程式碼  
    main()