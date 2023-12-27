from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Comment(models.Model):
    post = models.ForeignKey('myapp.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('main', 'Главное'),
        ('interesting', 'Интересное'),
        ('politic', 'Политика'),
        ('economy', 'Экономика'),
        ('culture', 'Культура'),
    ]

    title = models.CharField(max_length=200)
    preview = models.TextField(max_length=1024, default='')  # Маленькое описание новости с ограничением по длине
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            # Открываем изображение с использованием библиотеки Pillow
            img = Image.open(self.image.path)

            # Устанавливаем новый размер (например, 300x300 пикселей)
            new_size = (500, 500)
            img.thumbnail(new_size)

            # Сохраняем измененное изображение
            img.save(self.image.path)

    def comments_count(self):
        return self.comments.filter().count()

    def __str__(self):
        return self.title
