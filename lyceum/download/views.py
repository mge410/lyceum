from django.http import FileResponse
from django.http import HttpRequest
from django.conf import settings


def download_image(request: HttpRequest, file_name: str) -> FileResponse:
    file_name = str(settings.BASE_DIR) + file_name
    return FileResponse(open(file_name, 'rb'), as_attachment=True)