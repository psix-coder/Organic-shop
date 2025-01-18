from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to="menu/images/")

    def __str__(self):
        return self.name


class AllCaregories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
    slug = models.SlugField(max_length=150, unique=True)
    departments = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
    slug = models.SlugField(max_length=150, unique=True)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    allcategories = models.ForeignKey(AllCaregories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


TYPE_PRODUCT = {
    "kg": "KG",
    "g": "G",
    "l": "L",
    "ml": "Ml"
}

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3 , null=True, blank=True)
    quantiy = models.IntegerField(default=15)
    discount = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    type_product = models.CharField(max_length=150, choices=TYPE_PRODUCT.items())
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name