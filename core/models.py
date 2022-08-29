from django.db import models

class Escola(models.Model):
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=14)
    nome = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    cnpj =  models.CharField(max_length=14)

    def __str__(self):
        return f'{self.nome} ({self.email})'

class Usuario(models.Model):
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=14)
    nome = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    data_nasc = models.DateField()
    cpf =  models.CharField(max_length=12)

    def __str__(self):
        return f'{self.nome} ({self.cpf})'

class Crianca(models.Model):
    endereco = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    nome = models.CharField(max_length=150)
    escola = models.ForeignKey(
        Escola, on_delete=models.PROTECT, related_name="escolas"
    )
    data_nasc = models.DateField()
    cpf =  models.CharField(max_length=12)

    def __str__(self):
        return f'{self.nome} ({self.escola})'
    

