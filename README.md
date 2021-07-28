# News Provider API

## How to use the application.

- System Requirement:

        Docker version 20
        
- Create an .env file inside the projetct "docker folder":

        DEBUG = True (for development mode, False for production)

        POSTGRES_ENGINE=django.db.backends.postgresql
        POSTGRES_NAME=PostgreSQL
        POSTGRES_HOST=db
        POSTGRES_PORT=5432
        POSTGRES_USER=challenge
        POSTGRES_PASSWORD=challenge   

- To start the service:
    
        docker-compose up --build

- Run Python test:
    
        docker exec -it news-api python manage.py test

## Authentication by Token.

For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:
 
        Authorization: Token <xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>
        Content-Type: application/json

## Admin User.

After creating a user, enter in django admin and set "isStaff" True, only Staff can manage the /admin/ endpoints.

- SuperUser is required to access the Django Admin.
     - docker exec -it news-api /bin/bash
     - python manage.py createsuperuser

## Documentation endpoint.

        /api/docs
