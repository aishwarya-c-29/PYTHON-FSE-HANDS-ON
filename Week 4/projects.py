from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

Create Student (POST)
POST /api/students/
{
    "name": "Riya",
    "age": 21,
    "course": "Computer Science"
}
Get All Students (GET)
GET /api/students/

Response:

[
    {
        "id": 1,
        "name": "Riya",
        "age": 21,
        "course": "Computer Science"
    }
]
Get One Student (GET)
GET /api/students/1/
Update Student (PUT)
PUT /api/students/1/
{
    "name": "Riya",
    "age": 22,
    "course": "Data Science"
}
Delete Student (DELETE)
DELETE /api/students/1/
