from django.db import models

# Create your models here.
class slider(models.Model):
    image = models.ImageField(upload_to='static/pics/%y/%m/%d/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class image(models.Model):
    image = models.ImageField(upload_to='static/gallery/%y/%m/%d/', null=True)
    image1 = models.ImageField(upload_to='static/gallery/%y/%m/%d/', null=True)
    image2 = models.ImageField(upload_to='static/gallery/%y/%m/%d/', null=True)
    
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class faq(models.Model):
    title = models.TextField(max_length=50)
    desc = models.TextField(max_length=150)
    title1 = models.TextField(max_length=50, null=True)
    desc1= models.TextField(max_length=150, null=True)
    
    def __str__(self):
        return self.title

class services_info(models.Model):
    image = models.ImageField(upload_to="static/services_pic/%m/%d")
    title = models.TextField(max_length=20)
    info = models.TextField(max_length=70)

    def __str__(self):
        return self.title

class index_image(models.Model):
    image = models.ImageField(upload_to='static/gallery/%y/%m/%d/', null=True)
    image1 = models.ImageField(upload_to='static/gallery/%y/%m/%d/', null=True)
    image2 = models.ImageField(upload_to='static/gallery/%y/%m/%d/', null=True)
    image3 = models.ImageField(upload_to='static/gallery/%y/%m/%d/', null=True)
    
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class personal_info(models.Model):
    title = models.TextField(max_length=50, null=True)
    contact_number = models.IntegerField(null=True)
    address = models.TextField(max_length=90, null=True)
    email_id = models.EmailField(max_length=50, null=True)
    footer_desc = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.title

class whychooseus(models.Model):
    title = models.TextField(max_length=80, null=True)
    image = models.ImageField(null=True)
    info = models.TextField(max_length=200, null=True)
    image1 = models.ImageField(null=True)
    info1 = models.TextField(max_length=200, null=True)
    image2 = models.ImageField(null=True)
    info2 = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.title

class socialmediaaccount(models.Model):
    title = models.TextField(max_length=100, null=True)
    twitter = models.TextField(max_length=100, null=True)
    instagram = models.TextField(max_length=100, null=True)
    facebook = models.TextField(max_length=100, null=True)
    printest = models.TextField(max_length=100, null=True)
    whatsapp = models.TextField(max_length=100, null=True)    

    def __str__(self):
        return self.title