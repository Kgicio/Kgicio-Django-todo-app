# Kgicio-Django-todo-app-for-Algo-bulls
Created a todo application where we can add tasks,read,update and delete tasks according to their id. Their are five fields mainly(all the details in models.py file)-
title,description,the task creation time which cannot be edited,the due date of the task which can be edited and the status of the task.We can fire urls to get our work done.
log in-
started the server and fired the url 'localhost:8000/admin/' and entered the credentials.
add a task-
url- 'localhost:8000/api/task-create/'
In the box given enter the details of the 5 fields title,description,created,due_date,status in json format one by one.
read-
url- 'localhost:8000/api/task-list' to view all the tasks.
read a single task
url- 'localhost:8000/api/task-detail/<id>'.
delete a task-
url- 'localhost:8000/api/task-delete/<id>' to delete a task according to id.
