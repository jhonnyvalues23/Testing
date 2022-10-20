# from ProjectConfig import app

# if __name__ == '__main__':
#     app.run(debug=True)
from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
