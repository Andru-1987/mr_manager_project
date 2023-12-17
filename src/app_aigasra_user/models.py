from pathlib import Path
from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin


class AigasraUserBase(models.Model):

    telefono = models.CharField(max_length=15, verbose_name="Teléfono",blank=True,null=True)
    celular = models.CharField(max_length=15, verbose_name="Celular",blank=True,null=True)
    email = models.EmailField(verbose_name="Email",blank=True,null=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre",blank=True,null=True)
    apellido = models.CharField(max_length=50, verbose_name="Apellido",blank=True,null=True)
    dni = models.PositiveIntegerField(primary_key=True)
    cuit = models.PositiveIntegerField(verbose_name="CUIT",blank=True,null=True)
    nombre_matricula = models.CharField(max_length=50, verbose_name="Nombre de Matrícula",blank=True,null=True)
    distribuidora = models.CharField(max_length=100, verbose_name="Distribuidora",blank=True,null=True)
    domicio_real = models.TextField(verbose_name="Domicilio Real",blank=True,null=True)
    dir_registracion = models.TextField(verbose_name="Dir. de Registración",blank=True,null=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento",blank=True,null=True)
    accept_terms = models.BooleanField(default=True, verbose_name="Aceptar términos y condiciones",blank=True,null=True)
    accept_aigasra_info = models.BooleanField(default=True, verbose_name="Aceptar recibir información de Aigasra",blank=True,null=True)
    image = models.ImageField(upload_to='user_images/', verbose_name='Image',blank=True,null=True)

    def get_attribute(self, attr_name):
        return getattr(self, attr_name, None)


class AigasraUserManager(BaseUserManager):
    def create_user(self, dni, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not dni:
            raise ValueError('Users must have an email address')

        user = self.model(
            dni=dni,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_staffuser(self, dni, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            dni=dni,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            dni=dni,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user





class AigasraUser(AigasraUserBase,AbstractBaseUser,PermissionsMixin):
    
    objects = AigasraUserManager()
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    groups = models.ManyToManyField(Group, related_name='custom_user_groups',blank=False)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions',blank=False)


    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = []

    def activate_user(self):
        self.is_active = True
        self.save()

    def deactivate_user(self):
        self.is_active = False
        self.save()
        
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    def __str__(self) -> str:
        return f"{self.dni} : {self.nombre}"


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin



class UserFile(models.Model):
    file = models.FileField(upload_to='user_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AigasraUser, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return f"File uploaded by {self.user} at {self.uploaded_at}"



    def filename_with_extension(self):
        path = Path(self.file.name)
        return f"{path.stem}{path.suffix}"


class CustomUserPermissions(models.Model):
    user = models.OneToOneField(AigasraUser, on_delete=models.CASCADE, related_name='custom_user_permissions')

    class Meta:
        permissions = [
            ("can_change_settings", "Can change settings"),
            # Añade más permisos según sea necesario
        ]



