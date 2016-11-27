from django.db import models

class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_title = models.CharField('Заголовок', max_length=200)
    article_taxt = models.TextField('Превью', max_length=200)
    article_text = models.TextField('Контент', max_length=200 )
    article_date = models.DateTimeField('Дата')
    article_likes = models.IntegerField('Лайки', default=0)

    def __unicode__(self):
        return self.article_title

    def get_absolute_url(self):
        return "articles/get/%i/" % self.id
