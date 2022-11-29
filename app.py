from flask import Flask , render_template 
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/admin/login')
def login(): 
    return render_template('login.html')

@app.route('/reservation')
def reserv():
    return render_template('reserv.html')

if __name__ == '__main__':
    app.run(debug=True)
    