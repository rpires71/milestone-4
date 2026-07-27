# The Procfile defines the processes required to run the application in the
# production environment. Deployment platforms such as Heroku read this file
# to determine which commands should be executed during deployment and when
# starting the web application.

# Apply any outstanding database migrations before the application starts,
# ensuring that the production database schema remains synchronised with the
# latest Django models on every deployment.
release: python manage.py migrate

# Start the Django application using Gunicorn, a production-ready WSGI
# application server that receives and processes incoming HTTP requests.
web: gunicorn fithub.wsgi
