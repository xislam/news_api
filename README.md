Настройка проекта :

1. способ первый

    установите вертуальное окружение ссылка для этого https://netpoint-dc.com/blog/python-venv-ubuntu-1804/ 

     после установки и активации вы скачайте покеты 
     
     
     скачивание пакетов по команде pip install -r requirements.txt



следуйщие команды идут по django миграции и запуск проекта 

       
       ./manage.py migrate 
       
       ./manage.py createsuperuser 
       
       ./manage.py runserver 0.0.0.0:8000 
       
       или в сетигс можете перенастроить ALLOWED_HOSTS = ["*"] на ALLOWED_HOSTS = ["127.0.0.1"] и команда ./manage.py runserver
       
   
   
  
 
 2 способ использовать докер 
 
 что ды был доступ к data 
 
    sudo chown -R $USER:$USER . 
   
 после команда для старта создания docker image 
 
    docker-compose up
    
остановите проект и  проведите подалуста миграции 
 
    sudo docker-compose run web_1 ./manage.py migratу 

и повторите  docker-compose up


# URL 


      
        0.0.0.0:8000:api/token/              'token_obtain_pair'
  
        
        0.0.0.0:8000/api/token/refresh/                  'token_refresh'
        
        0.0.0.0:8000/user/create/              'create_user'
        
        0.0.0.0:8000/news/         'list all news, or create a new new.'


#Примерные настройки для поставки проекта на сервер 

ссылка по этой части которые я использовал для поставки 

https://www.alibabacloud.com/blog/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04_594319





