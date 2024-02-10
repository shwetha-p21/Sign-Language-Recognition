from flask import Flask,Blueprint
from flask import render_template


app = Flask(__name__)
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/home',methods=['POST','GET'])
def home():  
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)

#assets/vendor/bootstrap/css/bootstrap.min.css
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta nme="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Comptible" content="ie=edge">
            
# </head>
# <body>
#     <p>hello world</p>
    
#     <input type="button" id='script' name="scriptbutton" value="Capture vedio" onclick="exec('test.py');">
# </body>
    
# </html>

# assets/vendor/bootstrap/css/bootstrap.min.css