from django.db import models


class Cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    mensagem = models.TextField()

    def __str__(self):
        template = '{0.nome} {0.email} {0.telefone} {0.mensagem}'
        return template.format(self)


class Imovel(models.Model):
    TIPO_CHOICE = (
        ('Apartamento', 'Apartamento'),
        ('Casa', 'Casa'),
        ('Terreno', 'Terreno'),
    )

    CATERGORIA_IMOVEL_CHOICE = (
        ('Apartamento', 'Apartamento'),
        ('Casa', 'Casa'),
        ('Destaque', 'Destaque'),
    )
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    ID_Imovel = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    # imagens
    imagem1 = models.ImageField(
        upload_to="img_imoveis/%y", blank=False, null=False)
    imagem2 = models.ImageField(
        upload_to="img_imoveis/%y", blank=False, null=False)
    imagem3 = models.ImageField(
        upload_to="img_imoveis/%y", blank=False, null=False)
    imagem4 = models.ImageField(
        upload_to="img_imoveis/%y", blank=False, null=False)
    titulo = models.CharField(max_length=100)
    # informação
    informacao = models.TextField(max_length=2000, help_text="Descrição")
    area = models.IntegerField()
    quartos = models.IntegerField()
    banheiro = models.IntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    # Localidade
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=UF_CHOICES)
    categoria = models.CharField(
        max_length=100, choices=CATERGORIA_IMOVEL_CHOICE)
    tipo = models.CharField(
        max_length=100, choices=TIPO_CHOICE)


class Depoimento (models.Model):
    ID_Depoimentos = models.AutoField(primary_key=True)
    imageDep = models.ImageField(
        upload_to="img_Depoimentos/%y", blank=False, null=False)
    nome_depoente = models.CharField(max_length=100, blank=False, null=False)
    cliente_Dep = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        template = '{0.ID_Depoimentos} - {0.nome_depoente} - {0.cliente_Dep}'
        return template.format(self)
