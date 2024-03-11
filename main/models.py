from django.db import models

# Create your models here.
class Hospital (models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


    def __str__(self):
        return self.name
    



class Patient(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    national_id = models.CharField(max_length=20)

    # Medical History
    allergies = models.TextField()
    medical_conditions = models.TextField()
    medications = models.TextField()
    surgical_history = models.TextField()

    # Vital Signs
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    body_temperature = models.FloatField()

    # Appointments and Scheduling
    appointment_date_time = models.DateTimeField()
    visit_history = models.TextField()
    procedures_tests = models.TextField()

    # Insurance Information
    insurance_provider = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=50)
    coverage_details = models.TextField()

    # Billing and Payments
    invoicing_details = models.TextField()
    payment_history = models.TextField()

    # Diagnostic Reports
    lab_test_results = models.TextField()
    imaging_reports = models.TextField()

    # Treatment Plans
    prescribed_medications = models.TextField(null=True)
    treatment_procedures = models.TextField(null=True)
    specialist_referrals = models.TextField(null=True)

    # Notes and Observations
    physician_notes = models.TextField(null=True)
    nurse_observations = models.TextField(null=True)
    progress_notes = models.TextField(null=True)

    # Emergency Contacts
    emergency_contact_name = models.CharField(max_length=255, null=True)
    emergency_contact_phone = models.CharField(max_length=20, null=True)

    # Consent Forms
    treatment_consent = models.BooleanField(default= True)
    data_sharing_consent = models.BooleanField(default=True)
    

    # Communication Logs
    communication_logs = models.TextField()


    #hospital registration 
    registered_by = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name

    