from  document_creator import app
from  document_creator.views import general, create_document, upload_document

def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(general.general)
    app.register_blueprint(create_document.create_documents)

    # All done!
    app.logger.info("Blueprints registered")
