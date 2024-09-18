from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    qtd_total = models.PositiveIntegerField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),)
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preço = models.FloatField()
    preço_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return f'item do {self.pedido}'
    
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'



# Models:
#     Pedido:
#         user - FK User
#         total - Float
#         status - Choices
#             ('A', 'Aprovado'),
#             ('C', 'Criado'),
#             ('R', 'Reprovado'),
#             ('P', 'Pendente'),
#             ('E', 'Enviado'),
#             ('F', 'Finalizado'),

#         ItemPedido:
#             pedido - FK pedido
#             produto - Char
#             produto_id - Int
#             variacao - Char
#             variacao_id - Int
#             preco - Float
#             preco_promocional - Float
#             quantidade - Int
#             imagem - Char
