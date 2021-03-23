"""
Django settings for SharkAPAMP project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c=scl@v9m)m(qh751@xl^v*5x(b=xc9isypgn4yisl7g94_#$#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Django rest framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # 使用Django的标准`django.contrib.auth`权限，
    # or allow read-only access for unauthenticated users.
    # 或允许未经身份验证的用户进行只读访问。
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmdb.apps.CmdbConfig',
    'api.apps.ApiConfig',
    'users.apps.UsersConfig',
    'db.apps.DbConfig',
    'crispy_forms',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SharkAPAMP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SharkAPAMP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 设置 Django 的缓存为  Redis
"""
1. 安装
pip install django-redis

2. 在 settings.py 中设置，如下：
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://172.16.153.130:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",  # 连接密码
        }
    }
}

3. 使用：
from django.core.cache import cache

# 设置键值对
cache.set("foo", "value", timeout=10)  # 设置一个键为 foo, 值为 value, 超时时间为 10 秒

# 获取键值对
cache.get('foo')

# 获取 TTL 值(超时时间)
cache.ttl('foo')

4. 优化，使用性能更好的解析器 hiredis
hiredis 是一个用 C 写的 Redis 客户端, 并且他的解析器可以用在 django-redis 中:

先安装
pip install Hiredis 

在添加到配置选项中
"OPTIONS": {
    "PARSER_CLASS": "redis.connection.HiredisParser",
}

其他操作是一样的
"""
# Redis 参考资料 http://django-redis-chs.readthedocs.io/zh_CN/latest/
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://172.16.153.130:6379/1",
        "OPTIONS": {
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},  # 设置默认的连接池，最大连接数 100
            "PARSER_CLASS": "redis.connection.HiredisParser",  # pip install Hiredis
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",  # 连接密码
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 1.8 之后的包名，都叫 zh-hans。 之前 zh-CN

TIME_ZONE = 'Asia/Shanghai'  # 时区

USE_I18N = True

USE_L10N = True

USE_TZ = False    # False 使用本地时间


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AUTH_USER_MODEL = 'db.UsersProfile'

MODULES_BASE_DIRS = os.path.join(BASE_DIR, 'octopus/modules/')

# 自定义模块的存放路径
MODULES_DIRS = {
        'ansible': os.path.join(MODULES_BASE_DIRS, 'ansible/'),
        'shell': os.path.join(MODULES_BASE_DIRS, 'shell/'),
        'salt': os.path.join(MODULES_BASE_DIRS, 'salt/'),
    }

# Mongo DB
MONGO_HOST = '172.16.153.130'
MONGO_PORT = 27017
MONGO_DB = 'qfedu'
MONGO_COLLECTION = 'ansible_result'

# Redis Con
REDSI_KWARGS_LPUSH = {"host": '172.16.151.130', 'port': 6379, 'db': 1}
REDSI_LPUSH_POOL = None


# Ansible and  Task

INVENTORY_FILE = "{}/conf/hostlist".format(BASE_DIR)
TASK_STATUS_CODE = {
        "1000": "任务已接收，正在进行参数信息校验...",
        "1001": "参数校验完毕，开始创建子集进程...",
        "1002": "子进程创建完毕，开始实例化 Ansible 对象",
        "1003": "Ansible 对象创建成功，准备传参给 Ansible 对象，并开始执行任务!",
        "1004": "任务执行中...",

        "2000": "任务已成功执行完毕！正在获取结果...",
        "2001": "获取结果完毕! 准备将任务结果写入 [ Mongo.qfedu.ansible_result ]...",
        "2002": "任务结果已写入 [ Mongo.qfedu.ansible_result ]...",

        "4000": "目前没有从数据库中查询到内容",
        "4002": "传入的参数mod_type不匹配！",
        "4003": "传入的参数不完整！",
        "4004": "主机信息有误！",
        "5001": "服务器内部错误！资源繁忙！",

}

from django.core.urlresolvers import reverse_lazy

# 用户登录 URL
LOGIN_URL = reverse_lazy('users:user_login')
# 登录成功后跳转的 URL
LOGIN_REDIRECT_URL = reverse_lazy('index')

# 用户退出登录后跳转的 URL
LOGOUT_REDIRECT_URL = LOGIN_URL
