from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from .validators import real_age

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20, unique=True)

    class Meta:
        verbose_name = 'тэги'
        verbose_name_plural = 'Тэг'

    def __str__(self):
        return self.tag


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField(
        'Фото',
        upload_to='birthdays_images',
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
    )
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint'
            ),
        )
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'
        ordering = ('-birthday', 'first_name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.birthday}'

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})


class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
