from django.db import models



class News_Model(models.Model):



    title = models.CharField(max_length=150, verbose_name='название')
    content = models.TextField(blank=True, verbose_name='контент') # blank означает, что если текст сообщения пустой, то там будет записана пустая строка

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата редактирования')

    '''auto_now_add означает, что при создании дата сохраняется только один раз
       auto_now означает, что при редактировании будет изменяться дата и время'''



    path_image = 'images/%Y/%m/%d/'
    photo = models.ImageField(upload_to=path_image, blank=True, verbose_name='изображения')

    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                 verbose_name='Категория')

    def __str__(self):
        return 'название новости: ' + str(self.title)

    def __repr__(self):
        return self.title

    class Meta():
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title', 'id']

class TypeWork(models.Model):
    title = models.CharField(max_length=350, verbose_name='Название вида работы')

    class Meta():
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'
        ordering = ['title']



class Name_Comp(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название организации')

    class Meta():
        verbose_name = 'Название организации'
        verbose_name_plural = 'Названия организации'
        ordering = ['title']



class Portfolio(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название проекта')
    content = models.TextField(blank=True, verbose_name='Описание проекта')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')



    path_image = 'images/%Y/%m/%d/'
    photo1 = models.ImageField(upload_to=path_image, blank=True, verbose_name='изображение 1')
    photo2 = models.ImageField(upload_to=path_image, blank=True, verbose_name='изображение 2')
    photo3 = models.ImageField(upload_to=path_image, blank=True, verbose_name='изображение 3')
    photo4 = models.ImageField(upload_to=path_image, blank=True, verbose_name='изображение 4')
    photo5 = models.ImageField(upload_to=path_image, blank=True, verbose_name='изображение 5')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                 verbose_name='Категория')

    def __str__(self):
        return 'название проекта ' + self.title

    def __repr__(self):
        return self.title

    class Meta():
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['title']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Additional_Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование фотографий', blank=True)

    pathsave = 'images/Photo/'
    image = models.ImageField(upload_to=pathsave, verbose_name='Изображение')

    def __str__(self):
        return 'Наименование ' + self.title

    def __repr__(self):
        return self.title

    class Meta():
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['title']

class Price(models.Model):
    price = models.CharField(max_length=100, verbose_name='Цена')

    pathsave = 'images/price'
    image = models.ImageField(upload_to=pathsave, verbose_name='изображение для ценника')
    name = models.CharField(max_length=100, verbose_name='Тип')

    def __str__(self):
        return 'Цена ' + self.price

    def __repr__(self):
        return self.price

    class Meta():
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ['name']

class Photo(models.Model):

    title = models.CharField(max_length=100, verbose_name='Наименование изображения')
    pathsave = 'images/Photo'
    image = models.ImageField(upload_to=pathsave, verbose_name='изображение')

    def __str__(self):
        return 'Наименование ' + self.title

    def __repr__(self):
        return self.title

    class Meta():
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['title']









