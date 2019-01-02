from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify


from .validators import validate_author_email
# Create your models here.

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private')
)

class PostModel(models.Model):
    id              = models.AutoField(primary_key=True)
    active          = models.BooleanField(default=True)
    title           = models.CharField(
                            max_length=250,
                            default='New Title',
                            #Cambiamos el nombre del campo cuando se despliega pero no en la base de datos
                            verbose_name='Post Title',
                            #definir que este campo es único para todas las instancias
                            unique=True,
                            #personalizar los mensajes de error
                            error_messages={
                                "unique": "This title is not unique, please try again"
                            },
                            #Incluir texto de ayuda
                            help_text="Must be unique title")
    slug            = models.SlugField(
                            null=True,
                            #blank, hace que el campo por ejemplo, aparezca en el admin y se pueda editar desde el admin
                            blank=True,
                            #si queremos que no se pueda editar desde el admin (ni desde un formulario), indicamos editable False
                            #editable=False
                            )
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_data    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)}
                                                        #incluímos un validator antes importado
    author_email    = models.CharField(max_length=240, validators=[validate_author_email], null=True, blank=True)

#Hacer override del method Save
    def save(self, *args, **kwargs):
#usar print, para que se vean mensajes en el terminarl, es como console.log en JS
        print("hola")
        if not self.slug and self.title:
            self.slug =slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return smart_text(self.title)

#Uso de Django Signals
def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("before")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)

def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("after safe")
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)
