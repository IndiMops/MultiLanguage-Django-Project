from django.db import models

class Author(models.Model):
    name = models.CharField("Ім'я автора", max_length = 72)
    country = models.CharField("Країна", max_length=72)
    books = models.ManyToManyField('Book', verbose_name = "Книги", related_name = "authors",  blank=True)
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"
    
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField("Назва видавництва", max_length = 72)
    author = models.ManyToManyField("Book", verbose_name = "Книги", related_name = "book_publisher",  blank=True)
    
    class Meta:
        verbose_name = "Видавець"
        verbose_name_plural = "Видавці"
        
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("Назва книги", max_length = 128)
    publication_year = models.IntegerField('Рік видання')
    publisher = models.ForeignKey(Publisher, models.SET_NULL, verbose_name="Видавець", null=True, blank=True)
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, verbose_name = "Автор", null=True, blank=True)
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    
    def __str__(self):
        if self.author is None:# перевіряємо чи книга має автора
            return f"{self.title} - Немає автора"
        else:
            return f"{self.title} - {self.author}"
    
