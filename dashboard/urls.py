from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.dashboard_login, name='login'),
    path('', views.dashboard_home, name='home'),
    path('gallery/', views.gallery_list, name='gallery'),
    path('seo/', views.seo_edit, name='seo_edit'),
    path('navigation/', views.navigation_edit, name='navigation_edit'),
    path('hero/', views.hero_edit, name='hero_edit'),
    path('stats/', views.stats_list, name='stats_list'),
    path('stats/new/', views.stat_edit, name='stat_new'),
    path('stats/<int:stat_id>/edit/', views.stat_edit, name='stat_edit'),
    path('stats/<int:stat_id>/delete/', views.stat_delete, name='stat_delete'),
    path('services/', views.services_list, name='services_list'),
    path('services/new/', views.service_edit, name='service_new'),
    path('services/<int:service_id>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:service_id>/delete/', views.service_delete, name='service_delete'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('testimonials/', views.testimonials_list, name='testimonials_list'),
    path('faqs/', views.faqs_list, name='faqs_list'),
    path('footer/', views.footer_edit, name='footer_edit'),
    path('final-word/', views.final_word_edit, name='final_word_edit'),
    path('logout/', views.logout_view, name='logout'),
]

