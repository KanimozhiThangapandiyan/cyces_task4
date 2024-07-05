from django.http import HttpResponse,JsonResponse
from django.views import View
from apps.cms.tasks import export_user_data
import time
from datetime import timedelta,datetime
from apps.cms.tasks import summaa
from apps.cms.tasks import bulk_upload_task
import io, csv

class ExportUserDataAPIView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        result = export_user_data.delay(user_id)
        #eta_time = datetime.now() + timedelta(seconds=60)
        #result = export_user_data.apply_async(args=[user_id], eta=eta_time)
        return HttpResponse(f"Task enqueued with ID: {result.id}")

class summa(View):
        def get(self, request, *args, **kwargs):
             result = summaa.delay()

             ss = result.get()
             return JsonResponse({"string":ss["s"]})

class BulkUploadView(View):
    # def post(self, request, *args, **kwargs):
    #     file_obj = request.FILES.get("file")
    #     if file_obj:
    #         paramFile = io.TextIOWrapper(file_obj.file)
    #         portfolio1 = csv.DictReader(paramFile)
    #         list_of_dict = list(portfolio1)
    #         result=bulk_upload_task(list_of_dict)
    #         return JsonResponse({"result":result})
    #     else:
    #         list_of_dict = None
    #         return JsonResponse({"message": "Check your file"})

     def get(self, request, *args, **kwargs):
          result = bulk_upload_task.delay()
          ss = result.get()
          return JsonResponse({"string":ss["s"]})
