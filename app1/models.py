from django.db import models
class Profession(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    habilitis = models.TextField('Навыки',default='SOME STRING')
    company = models.TextField('Компания', default='SOME STRING')
    salary = models.TextField('Оклад', default="Some string")
    region = models.TextField('Название региона', default="Название региона")
    date_vacancy = models.TextField('Дату публикации вакансии.', max_length=20, default="Дату публикации вакансии.")


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Table Profession'
# Create your models here.