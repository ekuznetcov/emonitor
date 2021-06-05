from app.api import bp
from flask import jsonify, request, Response, current_app, send_from_directory, redirect, url_for
import flask_cors
from werkzeug.utils import secure_filename
import os
from splitres import get_messtat_files, splitres


flask_cors.CORS(bp)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] == 'messtat'

@bp.route('/nodes/', methods=['GET'])
@flask_cors.cross_origin()
def get_nodes():
    path = current_app.config['DATA_FOLDER']
    return jsonify(get_messtat_files(path))
    

@bp.route('/nodes/statistics', methods=['GET'])
def get_node():
    path = request.args.get('path')
    return jsonify(splitres(path))

@bp.route('/nodes/', methods=['GET', 'POST'])
@flask_cors.cross_origin()
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    return jsonify("1")
