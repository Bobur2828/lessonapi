from django.db import models

class Women(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(blank=True)
    time_created=models.DateTimeField(auto_now_add=True)
    time_updated=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    cat=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name