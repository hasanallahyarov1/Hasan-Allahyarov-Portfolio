from flask import Flask, request, render_template
from ner import SpacyDocument

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        doc = SpacyDocument(text)
        entities_markup = doc.get_entities_with_markup()
        return render_template('result.html', entities_markup=entities_markup, text=text)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)