from .base import *  # noqa

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "theme/static"),
    os.path.join(BASE_DIR, "theme/static_src"),
    os.path.join(BASE_DIR, "app/static"),
]
