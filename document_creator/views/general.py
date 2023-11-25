from flask import request, Blueprint, Response, jsonify, current_app
import json

general = Blueprint('general', __name__)

#health route
@general.route("/health")
def check_status():
    return Response(response=json.dumps({
        "app": current_app.config["APP_NAME"],
        "status": "OK",
        "headers": request.headers.to_list(),
        "commit": current_app.config["COMMIT"]
    }),  mimetype='application/json', status=200)
