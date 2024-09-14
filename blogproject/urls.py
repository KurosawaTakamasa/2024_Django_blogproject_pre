from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #http(s)://ホスト名/以下のパスがadmin/にマッチした場合
    #admin.site.urlを呼び出し、Djangoの管理サイトを表示する
    path('admin/', admin.site.urls),
    
    #http(s)://ホスト名/へのアクセスはblogappの
    #URLconf(urls.py)を呼び出す
    path('', include('blogapp.urls')),
]

