# from django.http import HttpResponse
# from django.views import View
# from apps.cms.tasks import export_user_data

# class ExportUserDataAPIView(View):
#     def get(self, request, *args, **kwargs):
#         # Assuming you have a user_id parameter in the URL
#         user_id = request.GET.get('user_id')
        
#         # Enqueue the Celery task asynchronously
#         result = export_user_data.delay(user_id)
        
#         # Optionally, you can return a response to the client
#         return HttpResponse(f"Task enqueued with ID: {result.id}")


from celery import shared_task
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import io
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from apps.common.models import PersonalDetails,EducationAndCertifications,WorkDetails,EmploymentHistory,Awards,Preferences

#@shared_task
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

            # Generate PDF content
            pdf_content = self.generate_pdf(user_data)

            filename = f"{personal_details.first_name}_{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"

            # Return PDF response
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            response.write(pdf_content)

            return response
        except Exception as e:
            # Handle exceptions (e.g., user not found)
            return HttpResponse("Error: " + str(e), status=400)

    def generate_pdf(self, data):
        buffer = io.BytesIO()
        # Create a PDF document
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        # Convert data to list of lists for table creation
        table_data = [['Field', 'Value']]

        for model_instance in data:
            for field in model_instance._meta.fields:
                field_name = field.verbose_name.capitalize()
                field_value = getattr(model_instance, field.attname)
                table_data.append([field_name, field_value])

        # Create a table from data
        table = Table(table_data)
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

        elements.append(table)

        # Build PDF document
        doc.build(elements)
        pdf_content = buffer.getvalue()
        buffer.close()

        return pdf_content
# import json
# from django.urls import reverse
# from django.http import JsonResponse
# import os
# from django.conf import settings

# class ExportUserDataAPIView(View):
#     def get(self, request, *args, **kwargs):
#         user_id = kwargs.get('user_id')

#         try:
#             # Fetch user's data from all relevant models
#             personal_details = PersonalDetails.objects.get(id=user_id)
#             education_certifications = EducationAndCertifications.objects.filter(user_id=user_id)
#             work_details = WorkDetails.objects.filter(user_id=user_id)
#             employment_history = EmploymentHistory.objects.filter(user_id=user_id)
#             awards = Awards.objects.filter(user_id=user_id)
#             preferences = Preferences.objects.filter(user_id=user_id)

#             # Combine all data into a single list
#             user_data = [
#                 personal_details,
#                 *education_certifications,
#                 *work_details,
#                 *employment_history,
#                 *awards,
#                 *preferences
#             ]

#             # Generate PDF content
#             pdf_content = self.generate_pdf(user_data)

#             filename = f"{personal_details.first_name}_{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"

#             # Save PDF file to the server
#             file_path = os.path.join(settings.MEDIA_ROOT, filename)
#             with open(file_path, 'wb') as f:
#                 f.write(pdf_content)

#             download_url = request.build_absolute_uri(settings.MEDIA_URL + filename)


#             # Construct JSON response containing the file path
#             response_data = {
#                 'message': 'PDF generated successfully.',
#                 'file_name': file_path,
#                 'download_url': download_url
#             }

#             # Return JSON response
#             return JsonResponse(response_data)
#         except Exception as e:
#             # Handle exceptions (e.g., user not found)
#             return HttpResponse(json.dumps({"error": str(e)}), status=400)

#     def generate_pdf(self, data):
#         buffer = io.BytesIO()
#         # Create a PDF document
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         elements = []

#         # Convert data to list of lists for table creation
#         table_data = [['Field', 'Value']]

#         for model_instance in data:
#             for field in model_instance._meta.fields:
#                 field_name = field.verbose_name.capitalize()
#                 field_value = getattr(model_instance, field.attname)
#                 table_data.append([field_name, field_value])

#         # Create a table from data
#         table = Table(table_data)
#         table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
#                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

#         elements.append(table)

#         # Build PDF document
#         doc.build(elements)
#         pdf_content = buffer.getvalue()
#         buffer.close()

#         return pdf_content
