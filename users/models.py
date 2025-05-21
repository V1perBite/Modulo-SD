from datetime import timedelta
from django.utils import timezone 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, UserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    '''
    Custom user manager for the custom user model.
    '''
    #! crea un usuario con el email y la contraseña, asegurando que el email sea obligatorio
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    #! crea un superusuario con el email y la contraseña, asegurando que el email sea obligatorio
    #! y que el superusuario tenga permisos de administrador
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    

#! Este es tu modelo de usuario principal, basado en AbstractUser, pero personalizado para usar email como login.
class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    #! Definimos los tipos de usuario como constantes
    #! para evitar errores de escritura y facilitar el mantenimiento del código
    #! y la legibilidad del código

    ADMIN = 'administrador'
    CLIENTE = 'cliente'
    GERENTE = 'gerente'
    # Add any additional fields you want to include in your custom user model
    # For example, you can add a field for the user's profile picture
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    # You can also add a field for the user's bio
    # bio = models.TextField(blank=True, null=True)
    
    # Add any other fields as needed
    username = None
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    USER_TYPE_CHOICES = (

        (ADMIN, 'Administrador'),
        (CLIENTE, 'Cliente'),
        (GERENTE, 'Gerente'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=CLIENTE)
    
    objects = CustomUserManager()

#! este modelo esta vinculado al modelo de usuario, y se utiliza para almacenar la información del cliente
#! y la información de la membresia del cliente, si esta activa
class Cliente(models.Model):
    """
    Model representing a client.
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    entry_date = models.DateField(auto_now_add=True)
    
    """
           This section is for Membership
           The membership model is not yet defined, so we will leave it commented for now.
           When the membership model is defined, we can uncomment this section and use it.
           
           and all configuration for the membership model
    """
    
    # ? por el momento se deja el tipo de usuario, como membresia, mientras se define el modelo de membresia
    # ? membership = models.ForeignKey(Membership, on_delete=models.CASCADE, blank=True, null=True)
    type_of_membership = models.CharField(max_length=20, choices=User.USER_TYPE_CHOICES, default='cliente')
    membership_start = models.DateField(default=timezone.now)
    membership_end = models.DateField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.user_type != User.CLIENTE:
            self.user_type = User.CLIENTE
            self.user.save()
        if self.membership_start and not self.membership_end:
            self.membership_end = self.membership_start + timedelta(days=30)
            super().save(*args, **kwargs)
            

    def is_membership_active(self):
        """
        Check if the membership is active.
        """
        if self.membership_end:
            return self.membership_end and self.membership_end >= timezone.now().date()

    
    def __str__(self):
        return self.user.email
    


#! for now we will leave the others users as empty models
#! when the models are defined, we can uncomment this section and use it.





class Administrador(models.Model):
    pass

class Gerente(models.Model):
    pass



    
    
    