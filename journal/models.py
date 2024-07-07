from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='journal_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='entries')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title