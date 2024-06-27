# Game Application
This is a task management dashboard application built using Django for the backend and HTML, TailwindCSS, and jQuery for the frontend.
Tailwind CSS was added using CDN for faster development.

Commands below use `Linux OS`.

### Implementations:

1. Tasks can be Created, Updated or deleted 
2. Tasks can be searched, filtered from the dashboard
3. jQuery ajax loading of task is available
4. API to view tasks implemented also

### To launch this app on your system:

1. Navigate to your desktop (or any folder of your choice)
```
cd Desktop
```
2. Create a new folder/directory called `taskproject`
```
mkdir taskproject
```
3. Navigate into this new folder
```
cd taskproject
```
4. Create a new Python Virtual environment in the `taskproject` folder.
```
python3 -m venv ./taskvenv
```
5. Activate this new virtual environment
```
source taskvenv/bin/activate
```
6. Clone this git repo
```
git clone https://github.com/Jaye-python/taskproject.git
```
7. Move into the `taskproject` folder 
```
cd taskproject
```
8. Install dependencies; DB uses Django inbuilt SQLite; then MIGRATE
```
pip install -r requirements.txt
python manage.py migrate
```
9. Create `superuser` account. There is an existing Admin account with email: `bb@bb.com` and password `lagoslagos`
```
python manage.py createsuperuser
```
10. Launch application
```
python manage.py runserver
```
11. Login in to `http://127.0.0.1:8000/admin/` to manage the app
12. To check the API documentation, visit either of these:
```
http://127.0.0.1:8000/api/schema/swagger-ui/#/
http://127.0.0.1:8000/api/schema/redoc/
```
13. You can view the Task dashboard from the root URL
```
http://127.0.0.1:8000
```
14. You can sign up using the navigation on the right. The app uses `email` as `username` 
15. You can upload your profile picture by selecting the `Profile Update` button on the right
16. From the homepage Task Dashboard, you can `Add Task`, `Modify Tasks`, `View Task Details`, `Delete Tasks`
17. From the homepage Task Dashboard, you may `Search Tasks` by their titles, `Filter Tasks` by priority and sort
18. Click on the `Ajax Tasks` link on our left to see a page where you may load tasks by clicking the appropriate buttons based on their status and search for tasks async
19. You may go to following API endpoints to view tasks based on status
```
http://127.0.0.1:8000/tasks/in_progress/
http://127.0.0.1:8000/tasks/completed/
http://127.0.0.1:8000/tasks/overdue/
```
