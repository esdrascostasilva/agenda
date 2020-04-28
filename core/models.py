from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

# class representations database
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #por padrão, o django dá um nome a sua tabela. Vc pode alterar isso coforme abaixo
    class Meta:
        db_table = 'evento'

    # no banco, ao criar um evento ele traz com o nome Object. O cód abaixo retorna o nome do evento criado
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M') # %Y-%m-%dT%H:%M # %m-%dT-%Y%H:%M

    def get_evento_atrasado (self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False