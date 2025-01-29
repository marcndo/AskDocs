from flask import jsonify, request
import app
from app.utils import parse_pdf, parse_csv, scrape_url
from app.models import get_answer_from_model


@app.route('/upload', methods=['POST'])
def upload_document():
    file = request.files.get('file')
    file_type = request.files.get('file_type')
    if file_type == "pdf":
        content = parse_pdf(file)
    elif file_type == 'csv':
        content = parse_csv(file)
    else:
        return jsonify({"error": "Unsupported file type"}), 400
    question = request.form.get('question')
    answer = get_answer_from_model(question, content)
    return jsonify({'answer': answer})