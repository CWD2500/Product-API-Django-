from django.db import models
from django.contrib.auth.models  import User
# Create your models here.



class Categories(models.TextChoices):
	COMPUTER =  'conputer',
	FOOD     =  'food',
	KIDS     =  'kids',
	HOME     =  'home' 



class  Product(models.Model):
	name = models.CharField(max_length=255 , default=""  , blank=False)
	description = models.TextField(max_length=1000 , default="" , blank=False)
	price = models.DecimalField(max_digits=8 , decimal_places=2 , default=0)
	brand = models.CharField(max_length=200 , default="" , blank=False)
	category = models.CharField(max_length=40 , blank=False , choices=Categories.choices)
	ratings  = models.DecimalField(max_digits=4 , decimal_places=3 , default=0)
	stock = models.IntegerField(default=0)
	createAt = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User , null=True , on_delete=models.SET_NULL)

	def __str__(self):
		return self.name
