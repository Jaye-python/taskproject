# Task Management Application
This is a task management dashboard application built using Django for the backend and HTML, TailwindCSS, and jQuery for the frontend.
Tailwind CSS was added using CDN for faster development.

Commands below use `Linux OS`.

### REQUIRED ENVIRONMENT VARIABLES THAT SHOULD BE IN YOUR `.env` FILE
1. DEBUG=True
2. SECRET_KEY='django-insecure-785yh)y_f11k_5_j=u55+)@godmh$&sm=!=2yit&rz%t&kd)t2'
3. DATABASE_NAME=<>
4. DATABASE_USER=<>
5. DATABASE_PASS=<>
6. DATABASE_HOST=<>
7. DATABASE_PORT=<>

### INCLUDED IN THE REPO
1. Ansible playbook to install django on AWS EC2: [Ansible file](playbook.yml)
2. Docker compose file that will run Prometheus, Grafana, PgAdmin and the Django app: [Docker Compose file](docker-compose.yml)
3. Kubernetes files start with `kub`. Here is the K8 deployment for Django: [Django K8](kub_django.yml). There are K8 deployments for [Prometheus](kub_prom.yml) , [Grafana](kub_grafana.yml), [PgAdmin](kub_pgadmin.yml) and [PrometheusConfig](kub_prom_config.yml) 
4. Terraform IAC script to create an EC2, VPC and RDS instance: [Terraform Main script](main.tf); `variables.tf` not included

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
7. Move into the `taskproject` folder which is included in the downloaded repo
```
cd taskproject
```
8. Install dependencies; DB uses Django inbuilt SQLite; no need to run migration
```
pip install -r requirements.txt
```
9. Create `superuser` account. There is an existing Admin account with email: `bb@bb.com` and password `lagoslagos`
```
python manage.py createsuperuser
```
10. Launch application. You may also open the repo in VS Code by running `code .`
```
python manage.py runserver
```
11. Login in to `http://127.0.0.1:8000/admin/` to manage the app. Admin page has been created to perform CRUD functions for the app
12. To check the API documentation, visit either of these:
```
http://127.0.0.1:8000/schema/swagger-ui/#/
http://127.0.0.1:8000/schema/redoc/
```
13. You can view the Task dashboard from the root URL
```
http://127.0.0.1:8000
```
14. You can sign up using the navigation on the right. The app uses `email` as `username`. To login, provide your `email` as `username`
15. You can upload your profile picture by selecting the `Profile Update` button on the right
16. From the homepage Task Dashboard, you can `Add Task`, `Modify Tasks`, `View Task Details`, `Delete Tasks`
17. From the homepage Task Dashboard, you may `Search Tasks` by their titles, `Filter Tasks` by priority and sort
18. Click on the `Ajax Tasks` link on your left to see a page where you may load tasks by clicking the appropriate buttons based on their status and search for tasks async. This page uses jQuery to load tasks and search tasks
19. You may go to following API endpoints to view tasks based on status
```
http://127.0.0.1:8000/tasks/in_progress/
http://127.0.0.1:8000/tasks/completed/
http://127.0.0.1:8000/tasks/overdue/
```
