# SideProject01-PersonalWeb
個人獨立小型專案<br>
網址: <a href='http://r97221004.pythonanywhere.com/'>http://r97221004.pythonanywhere.com/</a> <br>
<img src="https://github.com/r97221004/SideProject01-PersonalWeb/blob/master/PersonalWeb/static/git.PNG"></img>

# 介紹
這是我的第一個個人獨立小型專案，目前支持的功能還不多，未來會持續加入新的功能。歡迎在裡面的留言版留言給我。
個人網站所用到的技術:
<ul>
  <li>程式語言: Python、SQL、Bash、HTML/CSS</li>
  <li>框架: Flask</li>
  <li>資料庫: SQLite</li>
  <li>版本控制: Git</li>
  <li>部屬: Pythonanywhere</li>
</ul>
主要包含以下幾個功能點:
<ul>
  <li>時間在地化，包含相對時間與絕對時間</li>
  <li>留言的功能</li>
  <li>留言的刪除</li>
  <li>登入登出系統，用戶認證</li>
  <li>動態的新增、修改、刪除</li>
  <li>虛擬數據的生成</li>
</ul>

# 啟動
使用 git clone 將程式碼下載到你的電腦且進入 SideProject01-PersonalWeb
```
$ git clone git@github.com:r97221004/SideProject01-PersonalWeb.git
$ cd SideProject01-PersonalWeb
```
建立且激活虛擬環境
```
python -m venv venv
source ./venv/Scripts/activate
```
下載依賴套件
```
pip install -r requirements.txt
```
建立資料庫資料表跟虛擬數據
```
flask initdb --drop
flask forge
```
建立管理員帳號密碼，帳號密碼自己決定
```
flask admin
```
啟動
```
flask run
```
# 參考資源
<ul>
  <li>Flask 入門教程, 李輝</li>
  <li>Flask Web 開發實戰, 李輝</li>
  <li>Flask 網頁開發, Miguel Grinberg</li>
  <li>網頁前端影片，彭彭</li>
  <li>Bootstrap 教程, 尚硅谷</li>
</ul>
