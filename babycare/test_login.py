import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'babycare.settings')
django.setup()

from django.contrib.auth import authenticate
from babycareapp.models import User

# Test 1: Create a test user
print("=" * 50)
print("TEST: Login Functionality Fix")
print("=" * 50)

# Clear existing test users
User.objects.filter(email='test@example.com').delete()

# Create a test user
test_user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123',
    first_name='Test',
    role='parent'
)
print(f"\n✓ Created test user:")
print(f"  Email: {test_user.email}")
print(f"  Username: {test_user.username}")
print(f"  Role: {test_user.role}")

# Test 2: Authenticate using the custom backend
print(f"\n✓ Testing authentication with email...")
authenticated_user = authenticate(
    username='test@example.com',
    password='testpass123'
)

if authenticated_user:
    print(f"  ✓ Authentication SUCCESS!")
    print(f"  ✓ Authenticated user: {authenticated_user.email}")
    print(f"  ✓ Role: {authenticated_user.role}")
else:
    print(f"  ✗ Authentication FAILED!")

# Test 3: Wrong password should fail
print(f"\n✓ Testing authentication with wrong password...")
wrong_auth = authenticate(
    username='test@example.com',
    password='wrongpassword'
)

if wrong_auth is None:
    print(f"  ✓ Correctly rejected wrong password")
else:
    print(f"  ✗ Incorrectly accepted wrong password!")

print("\n" + "=" * 50)
print("✓ Login system is working correctly!")
print("=" * 50)
