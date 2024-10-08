from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blogapp'

#URLパターンを登録するためのリスト
urlpatterns = [
    #http(s)://ホスト名/以下のパスが''(無し)の場合
    #viewsモジュール(views.pyファイル)のIndexViewを実行
    #URLパターン名は'index'
    path('', views.IndexView.as_view(), name='index'),
    
    path('blog-detail/<int:pk>',
         views.BlogDetail.as_view(), 
         name='blog_detail'),
    
    path('science-list/',
         views.ScienceView.as_view(),
         name='science_list'),

    path('dailylife-list/',
         views.DailylifeView.as_view(),
         name='dailylife_list'),
    
    path('music-list/',
         views.MusicView.as_view(),
         name='music_list'),
    
    path('contact/',
         views.ContactView.as_view(),
         name='contact'),
    
]
