from django.db import models

# creating a database called Author
class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

# creating a database named Blog
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# use title as a blog name
    def __str__(self):
        return self.title
    
