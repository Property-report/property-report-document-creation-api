import os

APP_NAME = os.environ['APP_NAME']

BUCKET_ID = os.environ['BUCKET_ID']
BUCKET_NAME = os.environ['BUCKET_NAME']
aws_access_key_id = os.environ['ACCESS_KEY']
aws_secret_access_key = os.environ['aws_SECRET_KEY']
DOCUMENT_API_URL= os.environ['DOCUMENT_API_URL']
CDN_URL = os.environ['CDN_URL']
google_maps_apikey = os.environ['google_maps_apikey']

doc_location= os.environ['doc_location']
FLASK_LOG_LEVEL = os.environ['FLASK_LOG_LEVEL']
MORTGAGE_API_URL = os.environ['MORTGAGE_API_URL']
INSURANCE_API_URL = os.environ['INSURANCE_API_URL']
property_information_api_url = os.environ['property_information_api_url']

LOGCONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            '()': ' document_creator.extensions.JsonFormatter'
        },
        'audit': {
            '()': ' document_creator.extensions.JsonAuditFormatter'
        }
    },
    'filters': {
        'contextual': {
            '()': ' document_creator.extensions.ContextualFilter'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        },
        'audit_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'audit',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'application': {
            'handlers': ['console'],
            'level': FLASK_LOG_LEVEL
        },
        'audit': {
            'handlers': ['audit_console'],
            'level': 'INFO'
        }
    }
}
