from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator

class Characters(models.Model):
    title = models.CharField(
        verbose_name='название героя',
        max_length=100,
        unique=True
    )
    is_premium = models.BooleanField(
        verbose_name='премиальный ли персонаж',
        default=False
    )
    img = models.ImageField(
        verbose_name='картинка',
        upload_to='characters_photos'
    )
    power = models.IntegerField(
        verbose_name='количество силы',
        default=500,
        validators=[
            MinValueValidator(0,message='Значение силы не может быть меньше нуля'),
            MaxValueValidator(1000,message = 'Значение силы не может первышать 1000')
        ]
    )

    def __str__(self) -> str:
        return f'name: {self.title} | power: {self.power} | is_prem: {self.is_premium}'
    
    class Meta:
        verbose_name = 'персонаж'
        verbose_name_plural = 'персонажи'
        ordering= ('title',)

class Map(models.Model):
    NOT_PICKED = 'ntpcd'
    DE_MIRAGE = 'mrg'
    DE_DUST2 = 'dd2'
    DE_ANCIENT = 'anc'
    DE_VERTIGO = 'vert'
    DE_ANUBIS = 'anbs'
    DE_CACHE = 'cch'
    DE_INFERNO = 'inf'
    DE_NUKE = 'nuke'
    
    MAPS_CHOISES = [
        (NOT_PICKED,'Не выбрано'),
        (DE_MIRAGE,'Mirage'),
        (DE_DUST2,'Dust 2'),
        (DE_ANCIENT,'Ancient'),
        (DE_VERTIGO,'Vertigo'),
        (DE_ANUBIS,'Anubis'),
        (DE_CACHE,'Cache'),
        (DE_INFERNO,'Inferno'),
        (DE_NUKE,'Nuke')
    ]
    choiced_map = models.CharField(
        max_length = 5,
        choices = MAPS_CHOISES,
        default=NOT_PICKED
    )

    def __str__(self) -> str:
        return self.choiced_map
    
    class Meta:
        verbose_name = 'карта'
        verbose_name_plural = 'карты'
        ordering = ('choiced_map',)

class GameRegime(models.Model):
    title = models.CharField(
        verbose_name='режим',
        max_length=50,
        unique=True
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'игровой режим'
        verbose_name_plural = 'игровые режимы'
        ordering = ('title',)
