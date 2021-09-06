from django.db import models

# Create your models here.

class Usuario(models.Model):
    servidor = models.CharField(max_length=6)
    invocador = models.CharField(max_length=500,primary_key=True)

class Jugador(models.Model):
    summon = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    id_summon = models.CharField(max_length=100, primary_key=True)
    accountId = models.CharField(max_length=100)
    level = models.IntegerField()
    ligaS = models.CharField(max_length=20 )
    ligaF = models.CharField(max_length=20)

class Partidas(models.Model):
    idSummon = models.ForeignKey(Jugador, null=False, blank=False,on_delete=models.CASCADE) 
    idGame = models.CharField(max_length=10, primary_key=True)

class Campeones(models.Model):
    nombre = models.CharField(max_length=100)
    idchamp = models.CharField(max_length=150,primary_key=True)
    title = models.CharField(max_length=1000)

class Items(models.Model):
    nombre = models.CharField(max_length=100)
    iditem = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=1500)

class Sumonerspells(models.Model):
    nombre = models.CharField(max_length=100)
    idspell = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=1500)

class Game(models.Model):
    idgame = models.ForeignKey(Partidas, null=False, blank=False,on_delete=models.CASCADE)
    KDA = models.CharField(max_length=100)
    Farmxmin = models.FloatField()
    lane = models.CharField(max_length=15)
    vision = models.IntegerField()
    pinks = models.IntegerField()

