BROKER_URL = 'amqp://guest@rabbitmq-01.local//'
CELERY_RESULT_BACKEND = 'amqp://guest@rabbitmq-01.local//'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']