from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته بندی")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to="category", null=True, blank=True, verbose_name="نمونه تصویر دسته بندی")
    #add slug
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام نویسنده")
    description = models.TextField(verbose_name="توضیحات/بیوگرافی",null=True, blank=True)
    image = models.ImageField(upload_to="author", null=True, blank=True, verbose_name="تصویر نویسنده")
    rate = models.FloatField(default=5, verbose_name='امتیاز')
    birth_date = models.DateField(null=True, blank=True, verbose_name="تاریخ تولد")
    death_date = models.DateField(null=True, blank=True, verbose_name="تاریخ مرگ")
    # slug
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name = "نام ناشر")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    rate = models.FloatField(default=5, verbose_name='امتیاز')
    books = models.IntegerField(default=3, verbose_name="تعداد کتاب های ناشر")
    image = models.ImageField(upload_to="publisher", null=True, blank=True, verbose_name="تصویر ناشر")
    #add slug
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "ناشر"
        verbose_name_plural = "ناشر ها"

class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام کتاب")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی")
    front_cover_image = models.ImageField(upload_to="book", verbose_name="تصویر جلد جلوی کتاب", null=True, blank=True)
    back_cover_image = models.ImageField(upload_to="book", verbose_name="تصویر جلد پشت کتاب", null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="نویسنده")
    translator = models.CharField(max_length=100, verbose_name="مترجم", null=True, blank=True)
    language = models.CharField(max_length=100, verbose_name="زبان")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="ناشر")
    pages = models.IntegerField(verbose_name="تعداد صفحات")
    weight = models.FloatField(verbose_name="وزن", help_text = 'به گرم')
    price = models.IntegerField(verbose_name = 'قیمت', help_text = 'به تومان')
    publish_date = models.DateField(verbose_name="تاریخ انتشار", help_text="تاریخ انتشار کتاب")
    description = models.TextField(verbose_name = 'خلاصه کتاب')
    stock = models.IntegerField(verbose_name = 'موجودی')
    sales = models.IntegerField(verbose_name = 'تعداد فروش', default = 0) #shuld be not editable 
    isbn = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="ISBN")
    rate = models.FloatField(default=5, verbose_name='امتیاز')
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name="url title", editable=False)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if ' ' in self.name:
            self.name = self.name.replace(' ', '-')
        self.slug = self.name
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/book/{self.slug}/"


    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"



