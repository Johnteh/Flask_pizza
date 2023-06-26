from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Pass the required route to the decorator.
@app.route("/hello")
def hello():
    return "Hello, Welcome to GeeksForGeeks"





    

if __name__ == '__main__':
    app.run(debug=True, port = 5555)



