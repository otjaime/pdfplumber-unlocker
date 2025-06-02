from flask import Flask, request, jsonify
import pdfplumber

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "PDF Plumber API is running!"})

@app.route("/unlock", methods=["POST"])
def unlock_pdf():
    uploaded_file = request.files["file"]
    input_path = "input.pdf"
    uploaded_file.save(input_path)
    
    text = ""
    with pdfplumber.open(input_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n\n"
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
