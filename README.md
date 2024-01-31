# Task Manager App
Welcome to the Task-Manager Django project! This project is built using Python Django, Django Rest Framework, MongoDB as Database and Django templates with Ajax as well as essential Javascript snippets.

## Features

- Users can register using email and password.
- Email OTP Registration system.
- create, and update tasks according to dates.
- Users can view Tasks on a Calendar for a User friedly experience.
- Delete finished Tasks.


## Getting Started

### Prerequisites

Before you start, make sure you have the following installed:

- Python 
- Django
- Django Rest Framework
- MongoDB GUI 

### Installation

1. Clone the repository:
     git clone https://github.com/Hananvc/Task-Manager.git 
2. Navigate to the project directory:
3. Install dependencies:
     pip install -r requirements.txt
     Requirments are as follows,

     asgiref==3.7.2
     Django==4.1.13
     django-environ==0.11.2
     djangorestframework==3.14.0
     djongo==1.3.6
     dnspython==2.4.2
     pymongo==3.12.1
     pytz==2023.3.post1
     sqlparse==0.2.4
     typing_extensions==4.9.0
     tzdata==2023.3
4. Create a MongoDB cluster database:
     Recommending to use MongoDB ATLAS
5. Setup Django Smtp
6. Add environment Variables in Project settings directory as following variable names:
     DEBUG=True
     SECRET_KEY=''
     EMAIL_HOST=smtp.gmail.com
     EMAIL_PORT=587
     EMAIL_HOST_USER=
     EMAIL_HOST_PASSWORD=

     #DATABASE
     MONGODB_HOST=
     MONGODB_NAME=
     MONGODB_USER=
     MONGODB_PASSWORD=
7. Run the local server:
     python manage.py runserver


Now, your Django Project should be up and running.

### Additional 

For those who want to skip the hassle of running the project locally, I recommend to follow the below URL.

https://homehaven.website/

