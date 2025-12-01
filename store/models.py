from django.db import models

class Category(models.Model):
    name = models.CharField("Nome da categoria", max_length=100)
    slug = models.SlugField("Slug", unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Nome do produto", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    description = models.TextField("Descrição", blank=True)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    discount = models.DecimalField("Desconto (%)", max_digits=5, decimal_places=2, default=0)
    stock = models.PositiveIntegerField("Estoque", default=0)
    tags = models.CharField("Tags", max_length=200, blank=True)
    image_url = models.URLField("URL da imagem", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    available = models.BooleanField("Disponível", default=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['name']

    def __str__(self):
        return self.name

    def price_after_discount(self):
        if self.discount:
            return self.price * (1 - self.discount / 100)
        return self.price
