from NewsBlog.models import NewsArticle

class SomeOther1(NewsArticle):
    class Meta:
        verbose_name = 'News Article'
        verbose_name_plural = 'Sortable News Articles'
        ordering = ['the_order']


    

class SomeOther3(NewsArticle):
    class Meta:
        verbose_name = 'News Article'
        verbose_name_plural = 'Sortable News Articles'
        ordering = ['the_order']


    