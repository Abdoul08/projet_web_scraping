from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.get('/')
def recherche():
    print('hello word')
    return render_template('index.html')

@app.route('/affichage')
def affichage():
    if request.method == 'POST':
        return 'hello world'
        
if __name__ == '__main__':
    app.run(debug=True)