from django.db.models import Model,CharField,PositiveIntegerField,DateField,ImageField

# Create your models here.
RATING = (
    ('1','*'),
    ('2','**'),
    ('3','***'),
    ('4','****'),
    ('5','*****')
)


class Books(Model):
    name=CharField(max_length=20)
    author=CharField(max_length=20)
    catogary=CharField(max_length=20)
    published_date=DateField(null=True)
    pages=PositiveIntegerField(null=True)
    cover_image=ImageField(upload_to='images',null=True)
    rating=CharField(max_length=5,choices=RATING)


    def __str__(self):
        return self.author


    

