from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimony = models.CharField(max_length=500)

    class Meta:
        ordering = ('name', )
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'

    def __str__(self):
        return self.name


class Partners(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )
        verbose_name = 'partner'
        verbose_name_plural = 'partners'

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Category Name')

    class Meta:
        ordering = ('cat_name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.cat_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=150, verbose_name='Post Title')
    blog_img = models.ImageField(upload_to='images', verbose_name='Post Image')
    upload_date = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.ManyToManyField(Category, verbose_name='Category')
    content = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ('-upload_date',)

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        # self.slug = slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'


class Comment(models.Model):
    post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class About(models.Model):
    contentp1 = models.TextField(max_length=2000)
    content1image = models.ImageField(
        upload_to='images', verbose_name='pictures')
    contentp2 = models.TextField(max_length=2000)
    content2image = models.ImageField(
        upload_to='images', verbose_name='pictures')
    contentp3 = models.TextField(max_length=2000)
    content3image = models.ImageField(
        upload_to='images', verbose_name='pictures')

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'

    def __str__(self):
        return self.contentp1


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
