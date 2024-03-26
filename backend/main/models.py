import random
from django.db import models
from faker import Faker
from datetime import timedelta

fake = Faker()
# Create your models here.


class Hospital (models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[(
        'M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    email = models.EmailField(null=True, blank=True)  # Optional
    phone_number = models.CharField(
        max_length=20, null=True, blank=True)  # Optional
    emergency_contact_name = models.CharField(
        max_length=255, null=True, blank=True)  # Optional
    emergency_contact_phone = models.CharField(
        max_length=20, null=True, blank=True)  # Optional

    # Medical Information
    blood_type = models.CharField(max_length=10, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), (
        'B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], null=True, blank=True)
    allergies = models.CharField(
        max_length=255, null=True, blank=True)  # Summarized list

    # Hospital registration
    registered_by = models.ForeignKey(
        'Hospital', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.full_name}"


def create_mock_patient():
    full_name = fake.first_name() + " " + fake.last_name()

    date_of_birth = fake.date_object() - timedelta(days=fake.random.randint(30,
                                                                            365 * 100))  # Adjust max age as needed
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    chosen_blood_type = random.choice(blood_types)

    gender = 'M'
    email = fake.email()
    phone_number = fake.phone_number()
    emergency_contact_name = fake.name()
    emergency_contact_phone = fake.phone_number()
    blood_type = chosen_blood_type

    # Generate a comma-separated list of allergies
    allergies = ', '.join(fake.words(nb=2))

    return Patient(
        full_name=full_name,
        date_of_birth=date_of_birth,
        gender=gender,
        email=email,
        phone_number=phone_number,
        emergency_contact_name=emergency_contact_name,
        emergency_contact_phone=emergency_contact_phone,
        blood_type=blood_type,
        allergies=allergies,
    )
