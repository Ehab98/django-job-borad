from django.db import models

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
class Job(models.Model): #every class is a table 
    title =models.CharField(max_length=100) #column
    #location
    job_type =models.CharField(max_length=15 ,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at =models.DateTimeField(auto_now=True,editable=False)
    vacancy = models.IntegerField(default=1)
    salary =models.IntegerField(default=0)
    #category
    experience =models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
    


    



