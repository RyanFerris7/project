from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): 

    class NewManager(models.Manager):

        # The code below checks blog status and displays
        # only published articles.
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')  
    publish = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() # Default manager
    newmanager = NewManager() # Custom manager

    # The code below orders posts by published date. Changed to 
    # '-publish' to reverse order.
    class Meta:
        ordering = ('-publish',)

    # The code below returns the correct title to posts. 
    def __str__(self):
        return self.title
