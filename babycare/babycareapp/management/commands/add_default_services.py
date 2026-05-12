from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from babycareapp.models import Service

User = get_user_model()

class Command(BaseCommand):
    help = 'Add default services and providers to the database'

    def handle(self, *args, **options):
        # Create default providers if they don't exist
        providers_data = [
            {
                'email': 'sarah.nanny@example.com',
                'first_name': 'Sarah',
                'last_name': 'Johnson',
                'password': 'ServiceProvider123',
            },
            {
                'email': 'jessica.babysitter@example.com',
                'first_name': 'Jessica',
                'last_name': 'Smith',
                'password': 'ServiceProvider123',
            },
            {
                'email': 'michael.tutor@example.com',
                'first_name': 'Michael',
                'last_name': 'Brown',
                'password': 'ServiceProvider123',
            },
            {
                'email': 'emma.childcare@example.com',
                'first_name': 'Emma',
                'last_name': 'Davis',
                'password': 'ServiceProvider123',
            },
        ]

        providers = []
        for provider_data in providers_data:
            user, created = User.objects.get_or_create(
                email=provider_data['email'],
                defaults={
                    'username': provider_data['email'],
                    'first_name': provider_data['first_name'],
                    'last_name': provider_data['last_name'],
                    'role': 'provider',
                }
            )
            if created:
                user.set_password(provider_data['password'])
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created provider: {provider_data["first_name"]} ({provider_data["email"]})')
                )
                providers.append(user)
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Provider already exists: {provider_data["email"]}')
                )
                providers.append(user)

        # Create default services
        services_data = [
            {
                'title': 'Daytime Nanny Service',
                'description': 'Professional full-time nanny service for infants and toddlers. Experienced in child development and safety.',
                'location': 'New York, NY',
                'hourly_rate': 25.00,
                'provider_email': 'sarah.nanny@example.com',
            },
            {
                'title': 'Evening Babysitting',
                'description': 'Reliable evening and weekend babysitting services. Certified in CPR and First Aid.',
                'location': 'Brooklyn, NY',
                'hourly_rate': 20.00,
                'provider_email': 'jessica.babysitter@example.com',
            },
            {
                'title': 'Math & Science Tutoring',
                'description': 'Expert tutoring for grades K-12. Specializing in math, science, and test preparation.',
                'location': 'Manhattan, NY',
                'hourly_rate': 35.00,
                'provider_email': 'michael.tutor@example.com',
            },
            {
                'title': 'Preschool Preparation',
                'description': 'Help prepare your child for preschool. Focused on social skills, numbers, letters, and independence.',
                'location': 'Queens, NY',
                'hourly_rate': 30.00,
                'provider_email': 'emma.childcare@example.com',
            },
            {
                'title': 'Infant Care Specialist',
                'description': 'Specialized care for newborns and infants. CPR certified with experience in feeding, sleeping, and development.',
                'location': 'New York, NY',
                'hourly_rate': 28.00,
                'provider_email': 'sarah.nanny@example.com',
            },
            {
                'title': 'After School Daycare',
                'description': 'Safe and fun after-school care with homework help and recreational activities.',
                'location': 'Brooklyn, NY',
                'hourly_rate': 18.00,
                'provider_email': 'jessica.babysitter@example.com',
            },
            {
                'title': 'Language Learning Tutor',
                'description': 'English and Spanish language instruction for children. Interactive and engaging lessons.',
                'location': 'Manhattan, NY',
                'hourly_rate': 32.00,
                'provider_email': 'michael.tutor@example.com',
            },
            {
                'title': 'Special Needs Care',
                'description': 'Compassionate care for children with special needs. Trained in behavior support and developmental care.',
                'location': 'Bronx, NY',
                'hourly_rate': 40.00,
                'provider_email': 'emma.childcare@example.com',
            },
        ]

        created_count = 0
        for service_data in services_data:
            try:
                provider_email = service_data.pop('provider_email')
                provider = User.objects.get(email=provider_email)

                service, created = Service.objects.get_or_create(
                    title=service_data['title'],
                    provider=provider,
                    defaults={
                        'description': service_data['description'],
                        'location': service_data['location'],
                        'hourly_rate': service_data['hourly_rate'],
                        'is_available': True,
                    }
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Created service: {service_data["title"]} by {provider.first_name}')
                    )
                    created_count += 1
                else:
                    self.stdout.write(
                        self.style.WARNING(f'⚠ Service already exists: {service_data["title"]}')
                    )

            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error: Provider not found with email {provider_email}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error creating service {service_data["title"]}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Command completed! Created {created_count} new services.\n')
        )
        self.stdout.write(
            self.style.WARNING('Test Credentials:')
        )
        self.stdout.write('Email: sarah.nanny@example.com | Password: ServiceProvider123')
        self.stdout.write('Email: jessica.babysitter@example.com | Password: ServiceProvider123')
        self.stdout.write('Email: michael.tutor@example.com | Password: ServiceProvider123')
        self.stdout.write('Email: emma.childcare@example.com | Password: ServiceProvider123')
