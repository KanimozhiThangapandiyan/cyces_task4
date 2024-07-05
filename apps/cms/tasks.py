from celery import shared_task
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import io
from django.utils import timezone
from apps.common.models import PersonalDetails, EducationAndCertifications, WorkDetails, EmploymentHistory, Awards, Preferences
import time

@shared_task(queue='postman_queue')
def export_user_data(user_id):
    time.sleep(10)
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
        pdf_content = generate_pdf(user_data, personal_details)

        filename = f"{personal_details.first_name}_{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
        file_path = save_pdf_to_file(pdf_content, filename)
        #  # Return PDF response
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = f'attachment; filename="{filename}"'
        # response.write(pdf_content)
        # return response


        return {
            'task_id': str(export_user_data.request.id),  # Celery task ID
            'filename': filename,
            'status': 'success',  # Or any other status indicators
        }
    except Exception as e:
        # Handle exceptions (e.g., user not found)
        return {
            'task_id': str(export_user_data.request.id),
            'status': 'error',
            'message': str(e),
        }
def generate_pdf(data, personal_details):
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
def save_pdf_to_file(pdf_content, filename):
    file_path = f"/task4/dump.rdb/{filename}"
    with open(file_path, 'wb') as f:
        f.write(pdf_content)
    return file_path


@shared_task(queue='periodic_queue')
def summaa():
    s="kani"
    return {"s": s}

@shared_task(queue='bulk_upload_queue')
def bulk_upload_task():
    s="kani"
    return {"s": s}
    # try:
    #     for row in list_of_dict:
    #             if 'country_name' in row:
    #                 Country.objects.update_or_create(
    #                     country_name=row['country_name'],
    #                 )
    #                 count += 1
    #                 return f"Bulk upload completed. {count} countries added."
    # except Exception as e:
    #     return str(e)