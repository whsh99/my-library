# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:20:55 2022

@author: 陳永興
"""
import json  # 使用 json 函數
import random  # 使用 radom() 生成隨機書號
from books import Book  # 從 Books 模組導入 Book 類別
from datetime import datetime, timedelta  # 使用 datetime 函數生成借書/還書日期

class Books(object):
    
    def __init__(self):
        self.book_list = {}  # 初始化儲存書籍的字典 book_list
        self.json_list = self.read_json()   # 初始化儲存 json 檔案內容的串列
        
    def read_json(self):  # 第17行進行初始化的時候，讀取 json 檔案內容並回傳
        with open('library.json', 'r', encoding='utf-8') as f:  # 開啟並讀取 utf-8 編碼檔案
            book_json = json.load(f)  # 將 json 檔案內容載入
        return book_json
    
    def write_json(self):
        with open('library.json', 'w', encoding='utf-8') as f:  # 開啟並寫入 utf-8 編碼檔案
            # ensure_ascii = False: 讓 json 檔案中的中文正常顯示, indent = 2: json 檔案內容縮排2個字元
            f.write(json.dumps(self.json_list, ensure_ascii = False, indent = 2))
    
    def menu(self):  #列出選單所有功能
        print('【基本功能選單】')
        print('列出所有書籍:[1], 依類別查詢書籍:[2], 依書號查詢書籍:[3]')  # list_all(), query_type(), query_bn()
        print('【進階功能選單】')
        print('新增書籍:[4], 刪除書籍:[5], 修改書籍:[6]')  # add(), delete(), revise()
        print('【其它功能選單】')
        print('登出:[0]')  # exit()
        print('----------------')

    def random_book_num(self):  #隨機產生書號
        count = 0
        while count == 0:  # 檢查書號是否重複,若重複會再次隨機產生
            tmp_bn = random.randrange(10000, 99999)  # 隨機產生10,000到99,999之間的正整數來設定書號
            for n in self.json_list:
                if (n['bn'] == tmp_bn):
                    count = 0
                else:
                    return str(tmp_bn)

    def add(self):  # 新增書籍
        flag = 0
        while flag < 1:
            bn = self.random_book_num()  # 設定書號
            tl = input('請輸入書名: ')  # 設定書名
            # 設定書類型
            while True:
                typ = input('請輸入書類型(文學小說:[1]/藝術設計:[2]/人文社科:[3]/自然科普:[4]/電腦資訊:[5]): ')
                if typ == '1':
                    typ = '文學小說'
                    break
                if typ == '2':
                    typ = '藝術設計'
                    break
                if typ == '3':
                    typ = '人文社科'
                    break
                if typ == '4':
                    typ = '自然科普'
                    break
                if typ == '5':
                    typ = '電腦資訊'
                    break
                else:
                    print('請重新輸入!')
                    print('----------------')
            # 設定書語言
            while True:
                lang = input('請輸入書語言(zh[1]/en[2]): ')
                if lang == '1':
                    lang = 'zh'
                    break
                if lang == '2':
                    lang = 'en'
                    break
                else:
                    print('請重新輸入!')
            # 設定書狀態
            while True:
                stat = input('請輸入書狀態(在館藏:[1]/已外借:[2]): ')
                if stat == '1':
                    stat = '在館藏'
                    break
                if stat == '2':
                    stat = '已外借'
                    break
                else:
                    print('請重新輸入!')
                    print('----------------')
            # 設定借書/還書日期
            fmt = "%Y-%m-%d(%a)"  # 格式化日期
            now = datetime.now()  # 借書日期以系統當日時間設定
            future = now + timedelta(weeks = 1)  # 還書日期以借書日期1星期後設定
            if stat == '在館藏':  # 在館藏不設定借書日期
                b_date = ''
            else:
                b_date = now.strftime(fmt)  # 已外借會設定借書日期
            if stat == '已外借':  # 已外借會設定還書日期
                r_date = future.strftime(fmt)
            else:
                r_date = ''  # 在館藏便不設定還書日期
            # 將書籍屬性以字典儲存
            book_temp = {'bn': bn, 'tl': tl, 'typ': typ, 'lang': lang, 'stat': stat, 'b_date': b_date, 'r_date': r_date}
            book = Book(bn, tl, typ, lang, stat, b_date, r_date)  # 設定書籍物件的屬性,方便 print 第116行
            self.book_list[bn] = book_temp  # 使用字典儲存書籍,以書號 bn 作為 key
            self.json_list.append(book_temp)  # 將第111行的字典 append 到 json 檔案
            self.write_json()  # 寫入 json 檔案
            print('新增書籍成功!')
            print('書號: %s, 書名: %s, 書類型: %s, 書語言: %s, 書狀態: %s, 借書日期: %s, 還書日期: %s'
                  % (book.bn, book.tl, book.typ, book.lang, book.stat, book.b_date, book.r_date))
            
            n = 0
            while n < 1:
                choice = input('是否要繼續「新增書籍」(是:[y]/否:[n])? ')
                print('----------------')
                if (choice == 'y'):
                    flag = 0
                    n += 1
                if (choice == 'n'):
                    flag += 1
                    n += 1
                else:
                    print('請重新輸入!')
                    print('----------------')

    def list_all(self):  # 列出所有書籍
        flag = 0
        while flag < 1:
            typ1 = '文學小說'
            typ2 = '藝術設計'
            typ3 = '人文社科'
            typ4 = '自然科普'
            typ5 = '電腦資訊'
            
            print('所有 %s 類型的館藏書資訊: ' % typ1)
            i = 1
            for n in self.json_list:  # 讀取第17行初始化的串列
                if (n['typ'] == '文學小說'):
                    print(' (%d) 書號: %s, 書名: %s' % (i, n['bn'], n['tl']))
                    i += 1
            print('所有 %s 類型的館藏書資訊: ' % typ2)
            i = 1
            for n in self.json_list:
                if (n['typ'] == '藝術設計'):
                    print(' (%d) 書號: %s, 書名: %s' % (i, n['bn'], n['tl']))
                    i += 1
            print('所有 %s 類型的館藏書資訊: ' % typ3)
            i = 1
            for n in self.json_list:
                if (n['typ'] == '人文社科'):
                    print(' (%d) 書號: %s, 書名: %s' % (i, n['bn'], n['tl']))
                    i += 1
            print('所有 %s 類型的館藏書資訊: ' % typ4)
            i = 1
            for n in self.json_list:
                if (n['typ'] == '自然科普'):
                    print(' (%d) 書號: %s, 書名: %s' % (i, n['bn'], n['tl']))
                    i += 1
            print('所有 %s 類型的館藏書資訊: ' % typ5)
            i = 1
            for n in self.json_list:
                if (n['typ'] == '電腦資訊'):
                    print(' (%d) 書號: %s, 書名: %s' % (i, n['bn'], n['tl']))
                    i += 1
            print('----------------')
            
            n = 0
            while n < 1:
                choice = input('是否要繼續「列出所有書籍」(是:[y]/否:[n])? ')
                print('----------------')
                if (choice == 'y'):
                    flag = 0
                    n += 1
                if (choice == 'n'):
                    flag += 1
                    n += 1
                if (choice != 'y' and choice != 'n'):
                    print('請重新輸入!')
                    print('----------------')
    
    def query_type(self):  # 依類別查詢所有書籍
        flag = 0
        while flag < 1:
            while True:
                q_typ = input('請輸入想查詢的書類型(文學小說:[1]/藝術設計:[2]/人文社科:[3]/自然科普:[4]/電腦資訊:[5]): ')
                print('----------------')
                if q_typ == '1':
                    q_typ = '文學小說'
                    break
                if q_typ == '2':
                    q_typ = '藝術設計'
                    break
                if q_typ == '3':
                    q_typ = '人文社科'
                    break
                if q_typ == '4':
                    q_typ = '自然科普'
                    break
                if q_typ == '5':
                    q_typ = '電腦資訊'
                    break
                else:
                    print('請重新輸入!')
                    print('----------------')
            
            print('所有 %s 類型的館藏書資訊: ' % q_typ)
            
            count = 0  # 作為 flag 使用
            i = 1
            for n in self.json_list:
                if (n['typ'] == q_typ):
                    print(' (%d) 書號: %s, 書名: %s, 書類型: %s, 書語言: %s, 書狀態: %s, 借書日期: %s, 還書日期: %s'
                          % (i, n['bn'], n['tl'], n['typ'], n['lang'], n['stat'], n['b_date'], n['r_date']))
                    count = 1
                    i += 1
            print('----------------')
            if count == 0:
                print('找不到符合搜尋字詞「%s」的書類型。' % q_typ)
                print('----------------')
            
            n = 0
            while n < 1:
                choice = input('是否要繼續「輸入想查詢的書類型」(是:[y]/否:[n])? ')
                print('----------------')
                if (choice == 'y'):
                    flag = 0
                    n += 1
                elif (choice == 'n'):
                    flag += 1
                    n += 1
                else:
                    print('請重新輸入!')
                    print('----------------')
    
    def query_bn(self):  # 依書號查詢書籍
        flag = 0
        while flag < 1:
            q_bn = input('請輸入想查詢的書號: ')
            print('----------------')
            count = 0
            for n in self.json_list:
                if (n['bn'] == q_bn):
                    print('書號為 %s 的館藏書資訊: ' % n['bn'])
                    print('* 書名: %s, 書類型: %s, 書語言: %s, 書狀態: %s, 借書日期: %s, 還書日期: %s'
                          % (n['tl'], n['typ'], n['lang'], n['stat'], n['b_date'], n['r_date']))
                    count += 1
            print('----------------')
            if count == 0:
                print('找不到符合搜尋字詞「%s」的書號。' % q_bn)
                print('----------------')
            
            n = 0
            while n < 1:
                choice = input('是否要繼續「依書號查詢書籍」(是:[y]/否:[n])? ')
                print('----------------')
                if (choice == 'y'):
                    flag = 0
                    n += 1
                elif (choice == 'n'):
                    flag += 1
                    n += 1
                else:
                    print('請重新輸入!')
    
    def delete(self):  # 依書號刪除書籍
        flag = 0
        while flag < 1:
            q_bn = input('請輸入想刪除的書號: ')
            print('----------------')
            count = 0
            index = 0
            for n in self.json_list:
                if (n['bn'] == q_bn):
                    count = 1
                    del self.json_list[index]  # 將第17行串列中的元素刪除
                    self.write_json()  # 將刪除後的結果寫入 json 檔案
                    print('刪除成功!')
                index += 1
            if count == 0:
                print('找不到符合搜尋字詞「%s」的書號。' % q_bn)
                print('----------------')
            
            n = 0
            while n < 1:
                choice = input('是否要繼續「依書號刪除書籍」(是:[y]/否:[n])? ')
                print('----------------')
                if (choice == 'y'):
                    flag = 0
                    n += 1
                elif (choice == 'n'):
                    flag += 1
                    n += 1
                else:
                    print('請重新輸入!')
                    print('----------------')
                    
    def revise(self):  # 依書號修改書狀態,同時將借書日期和還書日期歸零/設定規定的日期
        flag = 0
        while flag < 1:
            r_bn = input('請輸入想修改的書號: ')
            print('----------------')
            count = 0
            index = 0
            alert = 0
            for n in self.json_list:
                if (n['bn'] == r_bn and count == 0 and alert == 0):
                    count = 1
                    print('開始修改書號為 %s 的館藏書資訊: ' % n['bn'])
                    while count == 1:
                        r_stat = input('請輸入書狀態(在館藏:[1]/已外借:[2]): ')
                        if r_stat == '1':
                            bn = n['bn']
                            tl = n['tl']
                            typ = n['typ']
                            lang = n['lang']
                            n_stat = '在館藏'  # 更新書狀態屬性
                            n_b_date = ''  # 借書日期歸零
                            n_r_date = ''  # 還書日期歸零
                            book_temp = {'bn': bn, 'tl': tl, 'typ': typ, 'lang': lang, 'stat': n_stat, 'b_date': n_b_date, 'r_date': n_r_date}
                            self.json_list.append(book_temp)
                            del self.json_list[index]  # 將第17行串列中的元素刪除
                            self.write_json()  # 將刪除後的結果寫入 json 檔案
                            print('修改書籍成功!')
                            print('----------------')
                            alert = 1
                            break
                        if r_stat == '2':
                            bn = n['bn']
                            tl = n['tl']
                            typ = n['typ']
                            lang = n['lang']
                            n_stat = '已外借'  # 更新書狀態屬性
                            fmt = "%Y-%m-%d(%a)"  # 格式化日期
                            now = datetime.now()  # 借書日期以系統當日時間設定
                            future = now + timedelta(weeks = 1)  # 還書日期以借書日期1星期後設定
                            n_b_date = now.strftime(fmt)  # 借書日期
                            n_r_date = future.strftime(fmt)  # 還書日期
                            book_temp = {'bn': bn, 'tl': tl, 'typ': typ, 'lang': lang, 'stat': n_stat, 'b_date': n_b_date, 'r_date': n_r_date}
                            self.json_list.append(book_temp)  # 將第111行的字典 append 到 json 檔案
                            del self.json_list[index]  # 將第17行串列中的原始元素刪除
                            self.write_json()  # 將更新的內容寫入 json 檔案
                            print('修改書籍成功!')
                            print('----------------')
                            count = 0
                            alert = 1
                            break
                        else:
                            count = 1
                            print('請重新輸入!')
                index += 1
            if alert == 0:
                print('找不到符合搜尋字詞「%s」的書號。' % r_bn)
                print('----------------')

            n = 0
            while n < 1:
                choice = input('是否要繼續「依書號修改書籍狀態」(是:[y]/否:[n])? ')
                print('----------------')
                if (choice == 'y'):
                    flag = 0
                    n += 1
                elif (choice == 'n'):
                    flag += 1
                    n += 1
                else:
                    print('請重新輸入!')
                    print('----------------')