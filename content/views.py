from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import (
    Hero, Stat, BrutalMathSection, BrutalMathStat, WhyCentauraSection,
    WhyCentauraFeature, Service, ComparisonTable, ComparisonTableFeature,
    PortfolioProject, PeopleBehindStrategy, WhyWeBuiltSection, ProcessSection,
    ProcessStep, FinalWordSection, Footer, SocialLink, MediaAsset, SEO, Navigation, FAQ, Testimonial
)
from .serializers import (
    HeroSerializer, StatSerializer, ServiceSerializer, PortfolioProjectSerializer,
    TestimonialSerializer, FAQSerializer, SEOSerializer, NavigationSerializer,
    FooterSerializer, SocialLinkSerializer, MediaAssetSerializer
)


@api_view(['GET'])
@permission_classes([AllowAny])
def homepage_data(request):
    """
    Aggregated endpoint that returns all homepage content in a single response.
    This matches the structure of the content seed JSON for easy React consumption.
    """
    # Hero
    hero = Hero.objects.first()
    hero_data = {
        'title': hero.title if hero else '',
        'subtitle': hero.subtitle if hero else '',
        'cta_text': hero.cta_text if hero else '',
        'cta_url': hero.cta_link if hero else '#',
        'background_image_url': hero.background_image if hero else '',
        'quote': hero.quote if hero else '',
        'founders': {
            'names': hero.founders_names if hero else '',
            'title': hero.founders_title if hero else '',
            'images': hero.founders_images if hero else [],
        }
    } if hero else {}

    # Stats
    stats = Stat.objects.all().order_by('sort_order')
    stats_data = [
        {'label': stat.label, 'value': stat.value}
        for stat in stats
    ]

    # Brutal Math
    brutal_math_section = BrutalMathSection.objects.first()
    brutal_math_stats = BrutalMathStat.objects.all().order_by('sort_order')
    brutal_math_data = {
        'title': brutal_math_section.title if brutal_math_section else '',
        'subtitle': brutal_math_section.subtitle if brutal_math_section else '',
        'statistics': [
            {'value': stat.value, 'description': stat.description}
            for stat in brutal_math_stats
        ],
        'closing_text': brutal_math_section.closing_text if brutal_math_section else '',
    } if brutal_math_section else {}

    # Why Centaura
    why_centaura_section = WhyCentauraSection.objects.first()
    why_centaura_features = WhyCentauraFeature.objects.all().order_by('sort_order')
    why_centaura_data = {
        'label': why_centaura_section.label if why_centaura_section else '',
        'title': why_centaura_section.title if why_centaura_section else '',
        'image_url': why_centaura_section.image_url if why_centaura_section else '',
        'features': [
            {'title': feature.title, 'description': feature.description}
            for feature in why_centaura_features
        ],
        'cta_text': why_centaura_section.cta_text if why_centaura_section else '',
        'cta_url': why_centaura_section.cta_url if why_centaura_section else '#',
    } if why_centaura_section else {}

    # Services
    services = Service.objects.all().order_by('sort_order')
    services_data = [
        {
            'label': service.label,
            'title': service.title,
            'description': service.description,
            'outcome': service.outcome,
        }
        for service in services
    ]

    # Comparison Table
    comparison_table = ComparisonTable.objects.first()
    comparison_features = ComparisonTableFeature.objects.filter(
        comparison_table=comparison_table
    ).order_by('sort_order') if comparison_table else []
    comparison_data = {
        'title': comparison_table.title if comparison_table else '',
        'subtitle': comparison_table.subtitle if comparison_table else '',
        'features': [
            {
                'name': feature.name,
                'typical': feature.typical,
                'centaura': feature.centaura,
            }
            for feature in comparison_features
        ],
        'cta_text': comparison_table.cta_text if comparison_table else '',
        'cta_url': comparison_table.cta_url if comparison_table else '#',
    } if comparison_table else {}

    # Case Studies (Portfolio Projects)
    case_studies = PortfolioProject.objects.filter(is_active=True).order_by('sort_order')
    case_studies_data = [
        {
            'category': project.category,
            'title': project.title,
            'description': project.description,
            'image_url': project.image_url,
        }
        for project in case_studies
    ]

    # People Behind Strategy
    people = PeopleBehindStrategy.objects.first()
    people_data = {
        'title': people.title if people else '',
        'intro': people.intro if people else '',
        'jane': {
            'name': people.jane_name if people else '',
            'title': people.jane_title if people else '',
            'image_url': people.jane_image_url if people else '',
            'bio': people.jane_bio if people else [],
        },
        'aimun': {
            'name': people.aimun_name if people else '',
            'title': people.aimun_title if people else '',
            'image_url': people.aimun_image_url if people else '',
            'bio': people.aimun_bio if people else [],
        },
        'cta_text': people.cta_text if people else '',
        'cta_url': people.cta_url if people else '#',
    } if people else {}

    # Why We Built
    why_built = WhyWeBuiltSection.objects.first()
    why_built_data = {
        'left': {
            'title': why_built.left_title if why_built else '',
            'content': why_built.left_content if why_built else [],
        },
        'right': {
            'title': why_built.right_title if why_built else '',
            'content': why_built.right_content if why_built else [],
        },
    } if why_built else {}

    # Process
    process_section = ProcessSection.objects.first()
    process_steps = ProcessStep.objects.filter(
        process_section=process_section
    ).order_by('sort_order') if process_section else []
    process_data = {
        'label': process_section.label if process_section else '',
        'title': process_section.title if process_section else '',
        'steps': [
            {
                'number': step.number,
                'title': step.title,
                'description': step.description,
            }
            for step in process_steps
        ],
        'cta_text': process_section.cta_text if process_section else '',
        'cta_url': process_section.cta_url if process_section else '#',
    } if process_section else {}

    # Final Word
    final_word = FinalWordSection.objects.first()
    final_word_data = {
        'label': final_word.label if final_word else '',
        'title': final_word.title if final_word else '',
        'content': final_word.content if final_word else [],
        'background_image': final_word.background_image if final_word else '',
        'cta_text': final_word.cta_text if final_word else '',
        'cta_url': final_word.cta_url if final_word else '#',
    } if final_word else {}

    # Footer
    footer = Footer.objects.first()
    footer_data = footer.content if footer else {}
    if footer:
        footer_data['copyright'] = footer.copyright_text

    # Image Gallery
    gallery_images = MediaAsset.objects.filter(folder='gallery').order_by('-created_at')[:4]
    image_gallery_data = [
        {
            'url': asset.url,
            'alt': asset.public_id,
        }
        for asset in gallery_images
    ]

    return Response({
        'hero': hero_data,
        'stats': stats_data,
        'brutal_math': brutal_math_data,
        'why_centaura': why_centaura_data,
        'services': services_data,
        'comparison_table': comparison_data,
        'case_studies': case_studies_data,
        'people_behind_strategy': people_data,
        'why_we_built': why_built_data,
        'process': process_data,
        'final_word': final_word_data,
        'footer': footer_data,
        'image_gallery': image_gallery_data,
    })


# Keep existing ViewSets for individual content management
class SEOViewSet(viewsets.ModelViewSet):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return one instance
        return SEO.objects.all()[:1]

    def perform_create(self, serializer):
        # If one exists, update it instead
        existing = SEO.objects.first()
        if existing:
            serializer.instance = existing
            serializer.save()
        else:
            serializer.save()


class NavigationViewSet(viewsets.ModelViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Navigation.objects.all()[:1]

    def perform_create(self, serializer):
        existing = Navigation.objects.first()
        if existing:
            serializer.instance = existing
            serializer.save()
        else:
            serializer.save()


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Hero.objects.all()[:1]

    def perform_create(self, serializer):
        existing = Hero.objects.first()
        if existing:
            serializer.instance = existing
            serializer.save()
        else:
            serializer.save()


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['sort_order', 'created_at']


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['sort_order', 'created_at']


class PortfolioProjectViewSet(viewsets.ModelViewSet):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['sort_order', 'created_at']


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['sort_order', 'created_at']


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['sort_order', 'created_at']


class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Footer.objects.all()[:1]

    def perform_create(self, serializer):
        existing = Footer.objects.first()
        if existing:
            serializer.instance = existing
            serializer.save()
        else:
            serializer.save()


class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['sort_order', 'created_at']


class MediaAssetViewSet(viewsets.ModelViewSet):
    queryset = MediaAsset.objects.all()
    serializer_class = MediaAssetSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['-created_at']

