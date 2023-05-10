import os
import dotenv
from django.core.asgi import get_asgi_application

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
dotenv.load_dotenv(dotenv_path)

APP_ENV = os.getenv("APP_ENV", "dev")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'fitzPrints.settings.{APP_ENV}')

application = get_asgi_application()
