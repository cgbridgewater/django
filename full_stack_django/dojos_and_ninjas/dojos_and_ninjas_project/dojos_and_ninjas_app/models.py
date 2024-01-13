from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f"Dojo: {self.name} - {self.city}"

    @classmethod
    def get_all_dojos(cls, data):
        return cls.objects.all()
    
    @classmethod
    def add_dojo(cls,data):
        return cls.objects.create(name=data['name'],city=data['city'],state=data['state'],desc=data['desc'])

    @classmethod
    def get_dojo_by_id(cls,id):
        return cls.objects.filter(id=id)



class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name = "ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f'Ninja: {self.first_name} {self.last_name}'

    @classmethod
    def get_all_ninjas(cls):
        return cls.objects.all()
    
    @classmethod
    def create_ninja(cls, data):
        return cls.objects.create(first_name=data['first_name'],last_name=data['last_name'],dojo=Dojo.get_by_id(data['dojo_id'])[0])
    
    @classmethod
    def get_ninja_by_id(cls,id):
        return cls.objects.filter(id=id)