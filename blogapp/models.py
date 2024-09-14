from django.db import models

class BlogPost(models.Model):
    '''モデルクラス 
    '''
    #タイトル用のフィールド
    title = models.CharField(
        max_length=200,
        verbose_name='タイトル'
        )
    
    #本文用のフィールド
    content = models.TextField(
        verbose_name='本文'
    )
    
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name= '投稿日時'
        )
    
    #カテゴリフィールド
    category = models.CharField(
        max_length=50, 
        choices=(('science', '科学のこと'), 
                 ('dailylife', '日常のこと'), 
                 ('music', '音楽のこと')),
        verbose_name='カテゴリ'
        )

    def __str__(self):
        '''Django管理サイトでデータを表示する際に識別名として、
           投稿記事のタイトルを表示するための処理
        '''
        return self.title