# my-library

## I. 專題簡介
依據題目要求，此系統使用 Python 實作，提供基本的圖書館管理功能，包含書籍的新增、刪除、修改、查詢以及管理者登入功能，並採用 JSON 檔案來儲存和讀取書籍資料。

## II. 功能和檔案說明

```=
├─ my-library
│ ├─ portal.py       # 主程式，作為系統入口並具備功能選單
│ ├─ admin.py        # 提供管理者帳號與密碼驗證相關功能
│ ├─ books.py        # 定義書籍物件
│ ├─ funs.py         # 實現書籍管理功能（新增、刪除、修改（借還書）和查詢等等）
│ └─ library.json    # 儲存圖書館書籍資料
```

### i. `portal.py`

作為系統的入口，以顯示主選單，並根據使用者輸入導向相應功能模組。

#### # 主要功能：

* 主功能選單。

### ii. `admin.py`

定義 Admin 類別，並提供登入和忘記密碼功能。

#### # 主要功能：

* `login()`：登入驗證，需輸入正確的帳號與密碼，最多可嘗試 3 次。
* `query_pwd()`：忘記密碼，提供學號驗證以提示密碼。

### iii. `books.py`

#### # 主要功能：

定義 Book 類別，並包含以下屬性：

* `bn`（書號，由`funs.py`之`random_book_num()`隨機產生5位數之書號。）
* `tl`（書名）
* `typ`（書類型，`1`：文學小說；`2`：藝術設計；`3`：人文社科；`4`：自然科普；`5`：電腦資訊。）
* `lang`（書語言，`1`：zh；`2`：en）
* `stat`（書狀態，`1`：在館藏；`2`：已外借）
* `b_date`（借書日期，格式化日期為`%Y-%m-%d(%a)`）
* `r_date`（還書日期，格式化日期為`%Y-%m-%d(%a)`）

### iv. `funs.py`

書籍管理模組。

#### # 主要功能：

1. `read_json` 和 `write_json`：從 JSON 檔案讀取與寫入書籍資料。
2. `menu()`：顯示所有功能的選單。
3. `list_all()`：列出館藏中的所有書籍。
4. `query_type()`和`query_bn()`：各別依類別或書號查詢書籍。
5. `add()`：新增書籍，新增一本書到館藏中並設定書籍屬性，同時自動生成隨機書號（`random_book_num()`）。
6. `delete()`：根據書號刪除指定書籍。
7. `revise()`：更新書籍狀態（例如：借閱或歸還）及日期。

### v. `library.json`

#### # 主要功能：

書籍資料儲存之檔案，範例內容如下所示：

```=JSON
[
  {
    "bn": "56026",
    "tl": "Do Androids Dream of Electric Sheep?",
    "typ": "文學小說",
    "lang": "en",
    "stat": "已外借",
    "b_date": "2022-10-12(Wed)",
    "r_date": "2022-10-19(Wed)"
  },
  ...
]
```

## III. 讀寫 JSON 檔案

在專題中，使用 Python 的 json 模組來讀取和寫入用於儲存圖書館所有書籍資料的 JSON 檔案。

```=
import json
```

首先，必須初始化用於儲存書籍資料的字典 `book_list`。接著，程式碼會呼叫 read_json() 方法，將 JSON 檔案的內容讀取並存入 list 型態的變數 `json_list`，`json_list` 中的每一個元素都是每一本以字典型態儲存的書。

```=python
def __init__(self):
    self.book_list = {}    # 初始化儲存書籍的字典 book_list
    self.json_list = self.read_json()    # 初始化儲存 json 檔案內容的串列
```

`read_json()` 方法從 library.json 讀取資料並回傳：

```=python
def read_json(self):  # 初始化字典的時候，讀取 json 檔案內容並回傳
    with open('library.json', 'r', encoding='utf-8') as f:  # 開啟並讀取 utf-8 編碼檔案
    book_json = json.load(f)  # 將 json 檔案內容載入
    return book_json
```

`write_json()` 則使用 UTF-8編碼寫入 JSON 檔案。

```=python
def write_json(self):
    with open('library.json', 'w', encoding='utf-8') as f:  # 開啟並寫入 utf-8 編碼檔案
    # ensure_ascii = False: 讓 json 檔案中的中文正常顯示, indent = 2: json 檔案內容縮排2個字元
    f.write(json.dumps(self.json_list, ensure_ascii = False, indent = 2))
```

查詢書籍

## IV. 安裝與使用
* 系統需求
Python 3.6 或以上版本。
* 安裝步驟
    1. 下載專題所有檔案到本機。
    2. 於 CMD 輸入以下指令執行程式：
        ```=bash
        python portal.py
        ```
* 操作說明
    * 登入系統：使用管理者帳號與密碼。
* 系統預設管理員帳號：
    * 帳號／密碼：lucas／123456（若連續三次輸入錯誤帳號或密碼，系統將強制退出至選單）。
