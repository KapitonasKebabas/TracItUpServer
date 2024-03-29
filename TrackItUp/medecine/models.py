from django.db import models
from cprofile.models import CustomUser as User

# Create your models here.
class AprovedMedecine(models.Model):
    name            = models.CharField(max_length=120, blank=False, null=False)
    description     = models.TextField(blank=True, null=True)
    is_prescription = models.BooleanField(default=True)
    photo           = models.ImageField()
    is_aproved      = models.BooleanField(default=False)

    def __str__(self):        
        return f"{self.name}"

class UserMedecine(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    medecine    = models.ForeignKey(AprovedMedecine, on_delete=models.DO_NOTHING)
    qty         = models.IntegerField(default=1)
    exp_date    = models.DateField()
    is_shared   = models.BooleanField(default=False)
    shared_qty  = models.IntegerField(default=1)

    def __str__(self):        
        return f"{self.user}: {self.medecine.name}"