from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Single-instance models (one per site)
class SEO(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    keywords = models.CharField(max_length=500, blank=True)
    og_image = models.URLField(blank=True, null=True)
    og_title = models.CharField(max_length=200, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

    def __str__(self):
        return self.title


class Navigation(models.Model):
    logo_text = models.CharField(max_length=100, blank=True, null=True)
    logo_image_url = models.URLField(blank=True, null=True)
    menu_items = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Navigation'
        verbose_name_plural = 'Navigation'

    def __str__(self):
        return "Navigation"


class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    background_image = models.URLField(blank=True, null=True)
    cta_text = models.CharField(max_length=100, blank=True, null=True)
    cta_link = models.URLField(blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    founders_names = models.CharField(max_length=200, blank=True, null=True)
    founders_title = models.CharField(max_length=100, blank=True, null=True)
    founders_images = models.JSONField(default=list, blank=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Hero'

    def __str__(self):
        return self.title


class BrutalMathSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    closing_text = models.TextField(blank=True, null=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brutal Math Section'
        verbose_name_plural = 'Brutal Math Section'

    def __str__(self):
        return self.title


class WhyCentauraSection(models.Model):
    label = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    image_url = models.URLField(blank=True, null=True)
    cta_text = models.CharField(max_length=200, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Why Centaura Section'
        verbose_name_plural = 'Why Centaura Section'

    def __str__(self):
        return self.title


class ComparisonTable(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    cta_text = models.CharField(max_length=200, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comparison Table'
        verbose_name_plural = 'Comparison Table'

    def __str__(self):
        return self.title


class WhyWeBuiltSection(models.Model):
    left_title = models.CharField(max_length=200, blank=True, null=True)
    left_content = models.JSONField(default=list, blank=True)
    right_title = models.CharField(max_length=200, blank=True, null=True)
    right_content = models.JSONField(default=list, blank=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Why We Built Section'
        verbose_name_plural = 'Why We Built Section'

    def __str__(self):
        return "Why We Built"


class ProcessSection(models.Model):
    label = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    cta_text = models.CharField(max_length=200, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Process Section'
        verbose_name_plural = 'Process Section'

    def __str__(self):
        return self.title


class FinalWordSection(models.Model):
    label = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.JSONField(default=list, blank=True)
    background_image = models.URLField(blank=True, null=True)
    cta_text = models.CharField(max_length=200, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Final Word Section'
        verbose_name_plural = 'Final Word Section'

    def __str__(self):
        return self.title


class PeopleBehindStrategy(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField(blank=True, null=True)
    jane_name = models.CharField(max_length=200, blank=True, null=True)
    jane_title = models.CharField(max_length=200, blank=True, null=True)
    jane_image_url = models.URLField(blank=True, null=True)
    jane_bio = models.JSONField(default=list, blank=True)
    aimun_name = models.CharField(max_length=200, blank=True, null=True)
    aimun_title = models.CharField(max_length=200, blank=True, null=True)
    aimun_image_url = models.URLField(blank=True, null=True)
    aimun_bio = models.JSONField(default=list, blank=True)
    cta_text = models.CharField(max_length=200, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'People Behind Strategy'
        verbose_name_plural = 'People Behind Strategy'

    def __str__(self):
        return self.title


class Footer(models.Model):
    copyright_text = models.CharField(max_length=200)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

    def __str__(self):
        return "Footer"


# Multi-instance models (many items)
class Stat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    icon = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Stat'
        verbose_name_plural = 'Stats'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return f"{self.value} - {self.label}"


class BrutalMathStat(models.Model):
    value = models.CharField(max_length=50)
    description = models.TextField()
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brutal Math Stat'
        verbose_name_plural = 'Brutal Math Stats'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return f"{self.value}"


class WhyCentauraFeature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Why Centaura Feature'
        verbose_name_plural = 'Why Centaura Features'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.title


class Service(models.Model):
    label = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    outcome = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.title


class ComparisonTableFeature(models.Model):
    comparison_table = models.ForeignKey(ComparisonTable, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=200)
    typical = models.BooleanField(default=False)
    centaura = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comparison Table Feature'
        verbose_name_plural = 'Comparison Table Features'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.name


class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Portfolio Project'
        verbose_name_plural = 'Portfolio Projects'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.title


class ProcessStep(models.Model):
    process_section = models.ForeignKey(ProcessSection, on_delete=models.CASCADE, related_name='steps')
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    description = models.TextField()
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Process Step'
        verbose_name_plural = 'Process Steps'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return f"{self.number} - {self.title}"


class MediaAsset(models.Model):
    public_id = models.CharField(max_length=255, unique=True)
    url = models.URLField(blank=True, null=True)
    secure_url = models.URLField(blank=True, null=True)
    web_url = models.URLField(blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    folder = models.CharField(max_length=200, default='uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Media Asset'
        verbose_name_plural = 'Media Assets'
        ordering = ['-created_at']

    def __str__(self):
        return self.public_id


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    rating = models.IntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.question


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.platform


# Legacy models (keeping for compatibility)
class Contact(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.title or "Contact"


class ContactInfo(models.Model):
    type = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return f"{self.label}: {self.value}"


class ContactFormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('email', 'Email'),
        ('tel', 'Phone'),
        ('textarea', 'Textarea'),
        ('select', 'Select'),
        ('checkbox', 'Checkbox'),
    ]
    
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=FIELD_TYPES, default='text')
    required = models.BooleanField(default=False)
    placeholder = models.CharField(max_length=200, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Form Field'
        verbose_name_plural = 'Contact Form Fields'
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.label

