from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# py manage.py makemigrations
# py manage.py migrate

# py manage.py collectstatic
# CharField (ограниченный текст), TextField (неограниченное количество текста), EmailField, URLField, IntegerField, DecimalField, BooleanField, DateTimeField, ForeignKey и ManyToMany

# бд домов
class House(models.Model):
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='home')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    floors = models.IntegerField()
    squareMeters = models.IntegerField()
    price = models.IntegerField()
    inDate = models.DateTimeField()

    def __str__(self):
        date = timezone.localtime(self.inDate)
        return f"{date.strftime('%A, %d %B, %Y at %X')}"

class UserHouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)