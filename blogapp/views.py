from django.shortcuts import render
#django.views.generic.baseからTemplateViewをインポート
from django.views.generic import ListView, DetailView, FormView
#モデルBlogPostをインポート
from .models import BlogPost 
#django.urlからreverse_lazyをインポート
from django.urls import reverse_lazy
#formモジュールからContactFormをインポート
from .forms import ContactForm
#django.contribからmessageをインポート
from django.contrib import messages
#django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

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

class ContactView(FormView):
    template_name = 'contact.html'
    
    form_class = ContactForm
    
    success_url = reverse_lazy('blogapp:contact')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        
        subject = f'お問い合わせ: {title}'
        message = f'送信者:{name}\nメールアドレス:{email}\nメッセージ:{message}'
        
        from_email = 'ymg2465999@stu.o-hara.ac.jp'
        
        to_list = ['takamasa.kurosawa@mail.o-hara.ac.jp']
        
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list)
        
        message.send()
        
        messages.success(self.request,
                         'お問い合わせは正常に送信されました')
        
        return super().form_valid(form)
    