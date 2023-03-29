from django.conf import settings
from django.http import FileResponse
from django.http import HttpRequest
from django.views.generic import View


class DownloadImageView(View):
    def get(self, request: HttpRequest, file_name: str) -> FileResponse:
        file_name = f'{str(settings.BASE_DIR)}{file_name}'
        return FileResponse(open(file_name, 'rb'), as_attachment=True)
