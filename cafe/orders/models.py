from django.db import models
from django.urls import reverse

# Create your models here.

# Таблица с блюдами
class ItemDish(models.Model):

    dish_id= models.IntegerField()
    title = models.CharField(max_length=100, db_index=True)
    price = models.IntegerField()
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

# Таблица с заказами в ORM
class Orders(models.Model):

    STATUS_CHOICES = {
        "В ожидании": "В ожидании",
        "Готово": "Готово",
        "Оплачено": "Оплачено",
    }

    order_id= models.IntegerField()
    table_number = models.IntegerField()
    items = models.OneToOneField(ItemDish, on_delete = models.CASCADE, primary_key = True)
    total_price = models.ImageField(blank=True)
    # slug = models.SlugField(max_length=255,unique=True, db_index=True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = "В ожидании")

    def __str__(self):
        return self.title

    class Meta:
        pass

    # def get_absolute_url(self):
    #     return reverse("post", kwargs={"post_slug": self.slug})




