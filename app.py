import io
from flask import Flask, render_template, request
from network import ClassifyImage
from PIL import Image

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    if 'image' not in request.files:
        error = 'No files found'
        return render_template('index.html', error=error)
    
    file = request.files['image']
    
    if(file):
        img = Image.open(io.BytesIO(file.read())).convert('RGB')
        
        classification = ClassifyImage(img)
        return render_template('index.html', classification=classification)
    
    error = 'Invalid file'
    return render_template('index.html', error=error)
    
if __name__ == '__main__':
    app.run(debug=True)