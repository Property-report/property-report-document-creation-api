from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")

app.logger.info(' document_creator')

from  document_creator.blueprints import register_blueprints
from  document_creator.exceptions import register_exception_handlers

# Register the exception handlers
register_exception_handlers(app)

register_blueprints(app)
