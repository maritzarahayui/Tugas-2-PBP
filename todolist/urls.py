from django.urls import path
from todolist.views import show_tasks
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete_task
from todolist.views import update_task
from todolist.views import get_todolist_json
from todolist.views import add_todolist_item

app_name = 'todolist'

urlpatterns = [
    path('', show_tasks, name='show_tasks'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
    path('delete_task/<int:i>/', delete_task, name='delete_task'),
    path('update_task/<int:i>/', update_task, name='update_task'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add_todolist_item, name='add_todolist_item'),
]