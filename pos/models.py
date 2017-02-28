from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

ACCESS_LEVELS = [
    ("s", "Garçom"),
    ("c", "Cozinheiro"),
    ("o", "Registrador")
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    nível_de_acesso = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    @property
    def is_owner(self):
        return self.nível_de_acesso == 'o'
    @property
    def is_cook(self):
        return self.nível_de_acesso == 'c'
    @property
    def is_server(self):
        return self.nível_de_acesso == 's'

@receiver(post_save, sender='auth.user')
def create_profile(sender, **kwargs):
    instance = kwargs["instance"]
    created = kwargs["created"]
    if created:
        Profile.objects.create(user=instance)

class FoodItem(models.Model):
    titulo = models.CharField(max_length=255)
    descrição = models.TextField()
    preço = models.FloatField()

    def __str__(self):
        return self.titulo

class Ticket(models.Model):
    table_number = models.DecimalField(max_digits=1, decimal_places=1, default="0")
    client_name = models.CharField(max_length=255, default="")
    created_by = models.ForeignKey('auth.user')
    created_time = models.DateTimeField(auto_now_add=True)
    is_placed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def total(self):
        return OrderItem.objects.filter(ticket=self.id).aggregate(Sum('lanches__preço')).get('lanches__preço__sum')

class OrderItem(models.Model):
    # numero da mesa com problemas
    lanches = models.ForeignKey(FoodItem)
    ticket = models.ForeignKey(Ticket)
    dados = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.lanches)
    @property
    def preço(self):
        return FoodItem.objects.get(titulo=self.lanches).preço
