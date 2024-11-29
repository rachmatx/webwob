from flask import Flask, render_template, request

app = Flask(__name__)

def create_app():
    app.config['SECRET_KEY'] = 'mkasmdkwei'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/homepage')
def base():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/barang')
def barang():
    return render_template('barang.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)