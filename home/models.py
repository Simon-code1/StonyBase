from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ("interlock", "Interlock"),
        ("masonry", "Masonry"),
        ("chimney", "Chimney Repair"),
        ("patio", "Patios & Walkways"),
        ("retaining_wall", "Retaining Walls"),
        ("stonework", "Custom Stonework"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    short_description = models.TextField()
    full_description = models.TextField(blank=True)
    image = models.ImageField(upload_to="projects/")
    location = models.CharField(max_length=150, blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
