from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime
from django.core.cache import cache
from django.urls import reverse
from datetime import datetime
from django.core.cache import cache


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def update_rating(self):
        total_post_rating = sum(post.rating * 3 for post in self.posts.all())
        total_comment_rating = sum(comment.rating for comment in self.comments.all())
        total_post_comment_rating = sum(comment.rating for post in self.posts.all() for comment in post.comments.all())
        self.rating = total_post_rating + total_comment_rating + total_post_comment_rating
        self.save()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('mails:news_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    POST_TYPES = [
        ('articles', 'Articles'),
        ('news', 'News'),
    ]
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def update_rating(self):
        total_comments_rating = sum(comment.rating for comment in self.comments.all())
        self.rating = total_comments_rating
        self.save()

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)














