from django.conf import settings

max_size = settings.FILE_UPLOAD_MAX_MEMORY_SIZE
print(f"Maximum file size: {max_size} bytes")