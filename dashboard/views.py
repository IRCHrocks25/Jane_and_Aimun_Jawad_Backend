from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
import json
from content.models import (
    Hero, Stat, Service, PortfolioProject, Testimonial, FAQ,
    SEO, Navigation, Footer, SocialLink, MediaAsset, FinalWordSection
)


def normalize_url(value):
    """Normalize URL values: convert '#' or empty string to None"""
    if not value or value.strip() == '' or value.strip() == '#':
        return None
    return value.strip()


@ensure_csrf_cookie
def dashboard_login(request):
    """Login view for dashboard"""
    if request.user.is_authenticated:
        if request.headers.get('Content-Type') == 'application/json':
            return JsonResponse({'success': True, 'redirect': '/dashboard/'})
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        # Handle JSON requests from React
        if request.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(request.body)
                username = data.get('username')
                password = data.get('password')
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        else:
            # Handle form submissions
            username = request.POST.get('username')
            password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'success': True, 'redirect': '/dashboard/'})
            next_url = request.GET.get('next', 'dashboard:home')
            return redirect(next_url)
        else:
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'error': 'Invalid username or password.'}, status=401)
            messages.error(request, 'Invalid username or password.')
    
    # Return CSRF token for GET requests (API calls from React)
    if request.headers.get('Accept') == 'application/json':
        from django.middleware.csrf import get_token
        csrf_token = get_token(request)
        response = JsonResponse({'csrf_token': csrf_token})
        # Set CSRF cookie explicitly for cross-origin requests
        response.set_cookie(
            'csrftoken', 
            csrf_token, 
            max_age=3600,
            samesite='Lax',
            httponly=False,
            secure=False
        )
        return response
    
    return render(request, 'dashboard/login.html')


@login_required
def dashboard_home(request):
    """Main dashboard overview page"""
    stats_count = Stat.objects.count()
    services_count = Service.objects.count()
    portfolio_count = PortfolioProject.objects.count()
    testimonials_count = Testimonial.objects.count()
    
    context = {
        'stats_count': stats_count,
        'services_count': services_count,
        'portfolio_count': portfolio_count,
        'testimonials_count': testimonials_count,
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def gallery_list(request):
    """Gallery/Media assets management"""
    assets = MediaAsset.objects.all().order_by('-created_at')
    return render(request, 'dashboard/gallery/list.html', {'assets': assets})


@login_required
def seo_edit(request):
    """SEO settings editor"""
    seo = SEO.objects.first()
    if not seo:
        seo = SEO.objects.create(
            title='Centaura Group',
            description='Strategic consultancy for exit planning',
        )
    
    if request.method == 'POST':
        seo.title = request.POST.get('title', '')
        seo.description = request.POST.get('description', '')
        seo.keywords = request.POST.get('keywords', '')
        seo.og_title = request.POST.get('og_title', '')
        seo.og_description = request.POST.get('og_description', '')
        seo.og_image = normalize_url(request.POST.get('og_image', ''))
        seo.save()
        return redirect('dashboard:seo_edit')
    
    return render(request, 'dashboard/seo/edit.html', {'seo': seo})


@login_required
def navigation_edit(request):
    """Navigation settings editor"""
    nav = Navigation.objects.first()
    if not nav:
        nav = Navigation.objects.create(logo_text='Centaura')
    
    if request.method == 'POST':
        nav.logo_text = request.POST.get('logo_text', '')
        nav.logo_image_url = normalize_url(request.POST.get('logo_image_url', ''))
        # Handle menu items as JSON
        import json
        menu_items = request.POST.get('menu_items', '[]')
        try:
            nav.menu_items = json.loads(menu_items)
        except:
            nav.menu_items = []
        nav.save()
        return redirect('dashboard:navigation_edit')
    
    return render(request, 'dashboard/navigation/edit.html', {'navigation': nav})


@login_required
def hero_edit(request):
    """Hero section editor"""
    hero = Hero.objects.first()
    if not hero:
        hero = Hero.objects.create(title='THE EXIT YOU DESERVE.')
    
    if request.method == 'POST':
        hero.title = request.POST.get('title', '')
        hero.subtitle = request.POST.get('subtitle', '')
        hero.background_image = normalize_url(request.POST.get('background_image', ''))
        hero.cta_text = request.POST.get('cta_text', '')
        hero.cta_link = normalize_url(request.POST.get('cta_link', ''))
        hero.quote = request.POST.get('quote', '')
        hero.founders_names = request.POST.get('founders_names', '')
        hero.founders_title = request.POST.get('founders_title', '')
        hero.save()
        return redirect('dashboard:hero_edit')
    
    return render(request, 'dashboard/hero/edit.html', {'hero': hero})


@login_required
def stats_list(request):
    """Stats list and management"""
    stats = Stat.objects.all().order_by('sort_order')
    return render(request, 'dashboard/stats/list.html', {'stats': stats})


@login_required
def stat_edit(request, stat_id=None):
    """Create or edit a stat"""
    stat = get_object_or_404(Stat, pk=stat_id) if stat_id else None
    
    if request.method == 'POST':
        if not stat:
            stat = Stat.objects.create(
                label=request.POST.get('label', ''),
                value=request.POST.get('value', ''),
                sort_order=int(request.POST.get('sort_order', 0)),
            )
        else:
            stat.label = request.POST.get('label', '')
            stat.value = request.POST.get('value', '')
            stat.sort_order = int(request.POST.get('sort_order', 0))
            stat.save()
        return redirect('dashboard:stats_list')
    
    return render(request, 'dashboard/stats/edit.html', {'stat': stat})


@login_required
@require_http_methods(["POST"])
def stat_delete(request, stat_id):
    """Delete a stat"""
    stat = get_object_or_404(Stat, pk=stat_id)
    stat.delete()
    return redirect('dashboard:stats_list')


@login_required
def services_list(request):
    """Services list and management"""
    services = Service.objects.all().order_by('sort_order')
    return render(request, 'dashboard/services/list.html', {'services': services})


@login_required
def service_edit(request, service_id=None):
    """Create or edit a service"""
    service = get_object_or_404(Service, pk=service_id) if service_id else None
    
    if request.method == 'POST':
        if not service:
            service = Service.objects.create(
                label=request.POST.get('label', ''),
                title=request.POST.get('title', ''),
                description=request.POST.get('description', ''),
                outcome=request.POST.get('outcome', ''),
                sort_order=int(request.POST.get('sort_order', 0)),
            )
        else:
            service.label = request.POST.get('label', '')
            service.title = request.POST.get('title', '')
            service.description = request.POST.get('description', '')
            service.outcome = request.POST.get('outcome', '')
            service.sort_order = int(request.POST.get('sort_order', 0))
            service.save()
        return redirect('dashboard:services_list')
    
    return render(request, 'dashboard/services/edit.html', {'service': service})


@login_required
@require_http_methods(["POST"])
def service_delete(request, service_id):
    """Delete a service"""
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    return redirect('dashboard:services_list')


@login_required
def portfolio_list(request):
    """Portfolio/Case studies list"""
    projects = PortfolioProject.objects.all().order_by('sort_order')
    return render(request, 'dashboard/portfolio/list.html', {'projects': projects})


@login_required
def testimonials_list(request):
    """Testimonials list"""
    testimonials = Testimonial.objects.all().order_by('sort_order')
    return render(request, 'dashboard/testimonials/list.html', {'testimonials': testimonials})


@login_required
def faqs_list(request):
    """FAQs list"""
    faqs = FAQ.objects.all().order_by('sort_order')
    return render(request, 'dashboard/faqs/list.html', {'faqs': faqs})


@login_required
def footer_edit(request):
    """Footer editor"""
    footer = Footer.objects.first()
    if not footer:
        footer = Footer.objects.create(copyright_text='© 2025 Centaura Group. All Rights Reserved.')
    
    if request.method == 'POST':
        footer.copyright_text = request.POST.get('copyright_text', '')
        footer.save()
        return redirect('dashboard:footer_edit')
    
    return render(request, 'dashboard/footer/edit.html', {'footer': footer})


@login_required
def final_word_edit(request):
    """Final Word section editor"""
    final_word = FinalWordSection.objects.first()
    if not final_word:
        final_word = FinalWordSection.objects.create(
            title='The Business You Build Determines the Options You Have',
            label='FINAL WORD'
        )
    
    if request.method == 'POST':
        final_word.label = request.POST.get('label', '')
        final_word.title = request.POST.get('title', '')
        final_word.background_image = normalize_url(request.POST.get('background_image', ''))
        # Handle content as JSON array (split by newlines)
        content_text = request.POST.get('content', '')
        final_word.content = [line.strip() for line in content_text.split('\n') if line.strip()] if content_text else []
        final_word.cta_text = request.POST.get('cta_text', '')
        final_word.cta_url = normalize_url(request.POST.get('cta_url', ''))
        final_word.save()
        return redirect('dashboard:final_word_edit')
    
    # Convert content array to text for editing
    content_text = '\n'.join(final_word.content) if final_word.content else ''
    
    return render(request, 'dashboard/final_word/edit.html', {
        'final_word': final_word,
        'content_text': content_text
    })


@login_required
def logout_view(request):
    """Logout and redirect to login"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('dashboard:login')

