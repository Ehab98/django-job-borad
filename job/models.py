from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify
'''
why i use model.Model ? 
answer :
    1-html widget
    2-validation
    3-db size 
'''
JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),

)

def image_upload(instance,filename):
    imagename ,extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)



class Job(models.Model): #every class is a table 
    title =models.CharField(max_length=100) #column
    #location
    job_type =models.CharField(max_length=15 ,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at =models.DateTimeField(auto_now=True,editable=False)
    vacancy = models.IntegerField(default=1)
    salary =models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience =models.IntegerField(default=1)
    image=models.ImageField(upload_to=image_upload)
    slug  =models.SlugField(blank=True,null=True)
    
    def save(self,*args, **kwargs):
        #logic
        self.slug =slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name =models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    



    

class Apply(models.Model):
    job =models.ForeignKey(Job,related_name='apply_job' ,on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    email =models.EmailField(max_length=254)
    website = models.URLField( max_length=200)
    cv = models.FileField(upload_to="apply/")
    cover_letter = models.TextField(max_length=300)
    created_at =models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name
    
    

