import json
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from content.models import (
    Hero, Stat, BrutalMathSection, BrutalMathStat, WhyCentauraSection,
    WhyCentauraFeature, Service, ComparisonTable, ComparisonTableFeature,
    PortfolioProject, PeopleBehindStrategy, WhyWeBuiltSection, ProcessSection,
    ProcessStep, FinalWordSection, Footer, SocialLink, MediaAsset
)


class Command(BaseCommand):
    help = 'Seed the database with initial homepage content from JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='content_seed/homepage_initial.json',
            help='Path to the JSON seed file (relative to backend directory)',
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        # Get the backend directory
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        full_path = os.path.join(backend_dir, file_path)
        
        if not os.path.exists(full_path):
            self.stdout.write(self.style.ERROR(f'File not found: {full_path}'))
            return

        with open(full_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        with transaction.atomic():
            # Hero
            self.stdout.write('Seeding Hero...')
            Hero.objects.all().delete()
            hero_data = data.get('hero', {})
            Hero.objects.create(
                title=hero_data.get('title', ''),
                subtitle=hero_data.get('subtitle', ''),
                background_image=hero_data.get('background_image_url', ''),
                cta_text=hero_data.get('cta_text', ''),
                cta_link=hero_data.get('cta_url', '#'),
                quote=hero_data.get('quote', ''),
                founders_names=hero_data.get('founders', {}).get('names', ''),
                founders_title=hero_data.get('founders', {}).get('title', ''),
                founders_images=hero_data.get('founders', {}).get('images', []),
            )

            # Stats
            self.stdout.write('Seeding Stats...')
            Stat.objects.all().delete()
            for idx, stat_data in enumerate(data.get('stats', [])):
                Stat.objects.create(
                    label=stat_data.get('label', ''),
                    value=stat_data.get('value', ''),
                    sort_order=idx,
                )

            # Brutal Math Section
            self.stdout.write('Seeding Brutal Math Section...')
            BrutalMathSection.objects.all().delete()
            brutal_math = data.get('brutal_math', {})
            brutal_math_section = BrutalMathSection.objects.create(
                title=brutal_math.get('title', ''),
                subtitle=brutal_math.get('subtitle', ''),
                closing_text=brutal_math.get('closing_text', ''),
            )
            
            BrutalMathStat.objects.all().delete()
            for idx, stat_data in enumerate(brutal_math.get('statistics', [])):
                BrutalMathStat.objects.create(
                    value=stat_data.get('value', ''),
                    description=stat_data.get('description', ''),
                    sort_order=idx,
                )

            # Why Centaura Section
            self.stdout.write('Seeding Why Centaura Section...')
            WhyCentauraSection.objects.all().delete()
            why_centaura = data.get('why_centaura', {})
            why_centaura_section = WhyCentauraSection.objects.create(
                label=why_centaura.get('label', ''),
                title=why_centaura.get('title', ''),
                image_url=why_centaura.get('image_url', ''),
                cta_text=why_centaura.get('cta_text', ''),
                cta_url=why_centaura.get('cta_url', '#'),
            )
            
            WhyCentauraFeature.objects.all().delete()
            for idx, feature_data in enumerate(why_centaura.get('features', [])):
                WhyCentauraFeature.objects.create(
                    title=feature_data.get('title', ''),
                    description=feature_data.get('description', ''),
                    sort_order=idx,
                )

            # Services
            self.stdout.write('Seeding Services...')
            Service.objects.all().delete()
            for idx, service_data in enumerate(data.get('services', [])):
                Service.objects.create(
                    label=service_data.get('label', ''),
                    title=service_data.get('title', ''),
                    description=service_data.get('description', ''),
                    outcome=service_data.get('outcome', ''),
                    sort_order=idx,
                )

            # Comparison Table
            self.stdout.write('Seeding Comparison Table...')
            ComparisonTable.objects.all().delete()
            comparison = data.get('comparison_table', {})
            comparison_table = ComparisonTable.objects.create(
                title=comparison.get('title', ''),
                subtitle=comparison.get('subtitle', ''),
                cta_text=comparison.get('cta_text', ''),
                cta_url=comparison.get('cta_url', '#'),
            )
            
            ComparisonTableFeature.objects.all().delete()
            for idx, feature_data in enumerate(comparison.get('features', [])):
                ComparisonTableFeature.objects.create(
                    comparison_table=comparison_table,
                    name=feature_data.get('name', ''),
                    typical=feature_data.get('typical', False),
                    centaura=feature_data.get('centaura', True),
                    sort_order=idx,
                )

            # Case Studies (Portfolio Projects)
            self.stdout.write('Seeding Case Studies...')
            PortfolioProject.objects.all().delete()
            for idx, case_data in enumerate(data.get('case_studies', [])):
                PortfolioProject.objects.create(
                    title=case_data.get('title', ''),
                    description=case_data.get('description', ''),
                    image_url=case_data.get('image_url', ''),
                    category=case_data.get('category', ''),
                    sort_order=idx,
                )

            # People Behind Strategy
            self.stdout.write('Seeding People Behind Strategy...')
            PeopleBehindStrategy.objects.all().delete()
            people = data.get('people_behind_strategy', {})
            PeopleBehindStrategy.objects.create(
                title=people.get('title', ''),
                intro=people.get('intro', ''),
                jane_name=people.get('jane', {}).get('name', ''),
                jane_title=people.get('jane', {}).get('title', ''),
                jane_image_url=people.get('jane', {}).get('image_url', ''),
                jane_bio=people.get('jane', {}).get('bio', []),
                aimun_name=people.get('aimun', {}).get('name', ''),
                aimun_title=people.get('aimun', {}).get('title', ''),
                aimun_image_url=people.get('aimun', {}).get('image_url', ''),
                aimun_bio=people.get('aimun', {}).get('bio', []),
                cta_text=people.get('cta_text', ''),
                cta_url=people.get('cta_url', '#'),
            )

            # Why We Built
            self.stdout.write('Seeding Why We Built Section...')
            WhyWeBuiltSection.objects.all().delete()
            why_built = data.get('why_we_built', {})
            WhyWeBuiltSection.objects.create(
                left_title=why_built.get('left', {}).get('title', ''),
                left_content=why_built.get('left', {}).get('content', []),
                right_title=why_built.get('right', {}).get('title', ''),
                right_content=why_built.get('right', {}).get('content', []),
            )

            # Process Section
            self.stdout.write('Seeding Process Section...')
            ProcessSection.objects.all().delete()
            process = data.get('process', {})
            process_section = ProcessSection.objects.create(
                label=process.get('label', ''),
                title=process.get('title', ''),
                cta_text=process.get('cta_text', ''),
                cta_url=process.get('cta_url', '#'),
            )
            
            ProcessStep.objects.all().delete()
            for idx, step_data in enumerate(process.get('steps', [])):
                ProcessStep.objects.create(
                    process_section=process_section,
                    number=step_data.get('number', ''),
                    title=step_data.get('title', ''),
                    description=step_data.get('description', ''),
                    sort_order=idx,
                )

            # Final Word
            self.stdout.write('Seeding Final Word Section...')
            FinalWordSection.objects.all().delete()
            final_word = data.get('final_word', {})
            FinalWordSection.objects.create(
                label=final_word.get('label', ''),
                title=final_word.get('title', ''),
                content=final_word.get('content', []),
                cta_text=final_word.get('cta_text', ''),
                cta_url=final_word.get('cta_url', '#'),
            )

            # Footer
            self.stdout.write('Seeding Footer...')
            Footer.objects.all().delete()
            footer_data = data.get('footer', {})
            Footer.objects.create(
                copyright_text=footer_data.get('copyright', ''),
                content=footer_data,
            )

            # Social Links
            self.stdout.write('Seeding Social Links...')
            SocialLink.objects.all().delete()
            for idx, link_data in enumerate(footer_data.get('contact', {}).get('social_links', [])):
                SocialLink.objects.create(
                    platform=link_data.get('platform', ''),
                    url=link_data.get('url', '#'),
                    sort_order=idx,
                )

            # Image Gallery (Media Assets)
            self.stdout.write('Seeding Image Gallery...')
            for idx, image_data in enumerate(data.get('image_gallery', [])):
                # Create a simple public_id from the URL
                url = image_data.get('url', '')
                public_id = f"gallery_{idx}_{url.split('/')[-1].split('?')[0]}"
                
                MediaAsset.objects.get_or_create(
                    public_id=public_id,
                    defaults={
                        'url': url,
                        'secure_url': url,
                        'web_url': url,
                        'thumbnail_url': url,
                        'folder': 'gallery',
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded all homepage content!'))

