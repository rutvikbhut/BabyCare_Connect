import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'babycare.settings')
django.setup()

from babycareapp.models import User
from django.db.models import Count

# Delete users with empty emails
deleted_count, _ = User.objects.filter(email='').delete()
print(f'✓ Deleted {deleted_count} users with empty emails')

# Delete duplicate emails (keep the first one)
duplicate_emails = User.objects.values('email').filter(email__gt='').annotate(count=Count('id')).filter(count__gt=1)
print(f'\nDuplicate emails found: {list(duplicate_emails)}')

for dup in duplicate_emails:
    users_with_email = list(User.objects.filter(email=dup['email']).order_by('id'))
    if len(users_with_email) > 1:
        # Delete all except the first one
        for user in users_with_email[1:]:
            user.delete()
        print(f'  Deleted {len(users_with_email) - 1} duplicate users with email: {dup["email"]}')

print('\n✓ Users after cleanup:')
for user in User.objects.all().values('id', 'username', 'email'):
    print(f"  {user}")

print(f'\n✓ Total users: {User.objects.count()}')

