from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.

class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published = Footballers.Status.PUBLISHED)


class Footballers(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0,'Черновик'
        PUBLISHED = 1,'Опубликовано'
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    content = models.TextField(blank=True)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]),x[1]),Status.choices)), default=Status.PUBLISHED)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,related_name='posts')
    tags = models.ManyToManyField('TagPost',blank=True,related_name='tags')
    wife = models.OneToOneField('Wife',on_delete=models.SET_NULL,null= True,blank=True,related_name='wif')
    
    objects = models.Manager()
    published = PublishManager()


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='Footballers'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})
    
""" def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)"""
    


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    class Meta:
        verbose_name_plural='Categorys'

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('category',kwargs={"cat_slug":self.slug})
    
class TagPost(models.Model):
    tag = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse('tag',kwargs={'tag_slug':self.slug})
    

class Wife(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True,default=0)
    

    def __str__(self) -> str:
        return self.name
    
    
        