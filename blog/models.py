from django.conf import settings  #他のファイルから何かをちょこっとずつ追加する行
from django.db import models
from django.utils import timezone


class Post(models.Model): #今回のモデルを定義します (これが オブジェクト),postはモデルの名前,models.Model はポストがDjango Modelだという意味
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

 #フィールドのタイプを決めなければいけません
 #models.CharField – 文字数が制限されたテキストを定義するフィールド
 #models.TextField – これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールドでしょ？
 #models.DateTimeField – 日付と時間のフィールド
 #models.ForeignKey – これは他のモデルへのリンク

    def publish(self): #ブログを公開するメソッドそのもの
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title