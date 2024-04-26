#from celery import shared_task
import csv
from django.http import HttpResponse
from django.views import View
from django.utils import timezone

from apps.common.models import PersonalDetails,EducationAndCertifications,WorkDetails,EmploymentHistory,Awards,Preferences

class ExportUserDataAPIView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')

        try:
            # Fetch user's data from all relevant models
            personal_details = PersonalDetails.objects.get(id=user_id)
            education_certifications = EducationAndCertifications.objects.filter(user_id=user_id)
            work_details = WorkDetails.objects.filter(user_id=user_id)
            employment_history = EmploymentHistory.objects.filter(user_id=user_id)
            awards = Awards.objects.filter(user_id=user_id)
            preferences = Preferences.objects.filter(user_id=user_id)

            # Combine all data into a single list
            user_data = [
                personal_details,
                *education_certifications,
                *work_details,
                *employment_history,
                *awards,
                *preferences
            ]

            # Generate CSV content
            response = self.generate_csv(user_data)

            return response
        except Exception as e:
            # Handle exceptions (e.g., user not found)
            return HttpResponse("Error: " + str(e), status=400)

    def generate_csv(self, data):
        fieldnames = ['Model', 'Field', 'Value']
        rows = []

        # Iterate over each model instance and its fields
        for model_instance in data:
            model_name = model_instance.__class__.__name__
            for field in model_instance._meta.fields:
                field_name = field.verbose_name.capitalize()
                field_value = getattr(model_instance, field.attname)
                rows.append({'Model': model_name, 'Field': field_name, 'Value': field_value})

        first_name = PersonalDetails.first_name
        print(first_name)
        filename = f"{first_name}_{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

        # Write CSV content
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

        return response
