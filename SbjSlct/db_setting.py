DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'admin',
        'PASSWORD': 'a42ads12754_',
        'HOST': 'chiak.cr3vvferpsff.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    },

}