from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index1():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/download.html')
def download():
    return render_template('download.html')

@app.route('/styles.css')
def serve_css():
    return send_from_directory(app.root_path + '/templates', 'styles.css')

@app.route('/a.jpg')
def anh():
    return send_from_directory(app.root_path + '/anh', 'a.jpg')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
