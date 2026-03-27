import sys
import os

# Add your project directory to the path
project_home = '/home/YOUR_USERNAME/CareerLink'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['PYTHONUNBUFFERED'] = '1'

# Import your Flask app
from app import app as application
