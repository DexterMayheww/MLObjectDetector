import io
from flask import Flask, render_template, request
from network import ClassifyImage
from PIL import Image

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file passed'
    
    file = request.files['image']
    
    if(file):
        img = Image.open(io.BytesIO(file.read())).convert('RGB')
        
        return f'Classification: {ClassifyImage(img)}'
    
if __name__ == '__main__':
    app.run(debug=True)