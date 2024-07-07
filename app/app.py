#flask web application
#flask is a lightweight web framework for Python

#app.py contains the logic of Flask web application. It sets up routes, loads the pre-trained model and tokenizer, and handle translation process

from flask import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# Load the pre-trained model and tokenizer
model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')
tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es')

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        text = request.form['text']
        translated_text = translate(text)
    return render_template('index.html', translated_text=translated_text)

def translate(text):
    tokens = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    translated_tokens = model.generate(**tokens)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

if __name__ == '__main__':
    app.run(debug=True)
