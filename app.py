from flask import Flask
from flask_restful import Api
from controllers.hotelsController import Hotels, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/hotels_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


def create_database():
    with app.app_context():
        db.create_all()
        print("Database created")

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<int:hotel_id>')

if __name__ == "__main__":
    from sql_alchemy import db
    db.init_app(app)
    create_database()
    app.run(debug=True)