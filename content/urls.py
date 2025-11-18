from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'seo', views.SEOViewSet, basename='seo')
router.register(r'navigation', views.NavigationViewSet, basename='navigation')
router.register(r'hero', views.HeroViewSet, basename='hero')
router.register(r'stats', views.StatViewSet, basename='stat')
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'portfolio', views.PortfolioProjectViewSet, basename='portfolio')
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'faqs', views.FAQViewSet, basename='faq')
router.register(r'footer', views.FooterViewSet, basename='footer')
router.register(r'social-links', views.SocialLinkViewSet, basename='sociallink')
router.register(r'media-assets', views.MediaAssetViewSet, basename='mediaasset')

urlpatterns = [
    path('homepage/', views.homepage_data, name='homepage-data'),
    path('', include(router.urls)),
]

