from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name='parent',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True,upload_to='categories/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True,upload_to='products/')
    categories = models.ManyToManyField('Category',verbose_name='category',)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.title

class File(models.Model):
    product = models.ForeignKey('Product',verbose_name='product',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    file = models.FileField(upload_to='files/%Y/%m/%d')

    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'
    
    def __str__(self):
        return self.title
