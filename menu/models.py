from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Attack(models.Model):
    at_id = models.AutoField(primary_key=True)
    at_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    damage = models.IntegerField(default=10)
    
    def __str__(self):
        return self.name



class Pokemon(models.Model):
    poke_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    poke_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    health = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    defense = models.IntegerField(default=10)
    speed = models.IntegerField(default=10)
    img = models.ImageField(upload_to='pokemon_images/', default='pokemon_images/default.png')

    attack1 = models.ForeignKey(Attack, related_name='attack1', on_delete=models.SET_NULL, null=True)
    attack2 = models.ForeignKey(Attack, related_name='attack2', on_delete=models.SET_NULL, null=True)
    attack3 = models.ForeignKey(Attack, related_name='attack3', on_delete=models.SET_NULL, null=True)
    attack4 = models.ForeignKey(Attack, related_name='attack4', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.name} (Type: {self.poke_type})"
