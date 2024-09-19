from django.shortcuts import render
#django.views.generic.baseからTemplateViewをインポート
from django.views.generic import ListView, DetailView
#モデルBlogPostをインポート
from .models import BlogPost 

class IndexView(ListView):
    #index.htmlをレンダリング(描画)する
    template_name = 'index.html'
    
    #BlogPostのオブジェクト(レコードの一覧)にorder_by()関数を適用して
    #BlogPostのレコードを登校日順の降順(大きい順=新しい順)に並べる
    queryset = BlogPost.objects.order_by('-posted_at')
    
    #1ページに表示するレコードの件数を表示
    paginate_by = 4

class BlogDetail(DetailView):
    #post.htmlをレンダリング(描画)する
    template_name = 'post.html'
    
    #参照するモデル(データベース)を指定
    model = BlogPost

class ScienceView(ListView):
    template_name ='science_list.html'
    
    context_object_name = 'science_records'
    
    queryset = BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    
    paginate_by = 2

class DailylifeView(ListView):
    template_name ='dailylife_list.html'
    
    context_object_name = 'dailylife_records'
    
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    
    paginate_by = 2
    
class MusicView(ListView):
    template_name ='music_list.html'
    
    context_object_name = 'music_records'
    
    queryset = BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    
    paginate_by = 2