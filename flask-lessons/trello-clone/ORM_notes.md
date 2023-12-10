
``` python #import flask
from flask import Flask
#import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#import date
from datetime import date 
#import json
import json
#import marshmallow - dealing with serialising models/objects
from flask_marshmallow import Marshmallow

#create app
app = Flask(__name__)


#configure SQLAlchemy
#print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello'

#this connects the app to the database
db = SQLAlchemy(app)
# print(db)
#create instance of Marshmallow and parse app
ma = Marshmallow(app)

#create Model - an object that represents a table in the database aka schema
class Card(db.Model):
    __tablename__ = 'cards' #plural table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    status = db.Column(db.String(30))
    date_created = db.Column(db.Date())

    #this is a way of avoiding using marshmallow - but got scrapped because you still can't extract just specific column fields etc)
    # def to_dict(self):
    #     return { 'id': self.id, 'title': self.title, 'description': self.description, 'status': self.status, 'date_created': self.date_created }


#creating a schema for Marshmallow serialisation
class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created')



#must be connect to app/flask scope, use @app.cli.command
@app.cli.command('db_create')
def db_create():
    #option for updates
    db.drop_all()
    #once table named cards then drop all ineffective can go to postgres and command drop table card(s) manually
    db.create_all()
    print('Created tables')

#seed the database with data
@app.cli.command('db_seed')
def db_seed():
    #create a list of cards card1, card2 etc becomes a list
    cards = [
    #card1 = Card(
        Card(
            title =  'Start the project',
            description = 'Stage 1 - Create ERD',
            status = 'Done',
            date_created = date.today(),
         ),

#ORM2 lesson we created more cards to seed the db
    #card2 = Card(
        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement CRUD queries',
            status = 'In Progress',
            date_created = date.today(),
        ),

    #card3 = Card(
        Card(
            title = 'Marshmallow',
            description = 'Stage 2 - Implement JSONify of models',
            status = 'In Progress',
            date_created = date.today(),
        ),
    ]


    # db.session.add(card1)
    # db.session.add(card2)
    # db.session.add(card3)
    db.session.add_all(cards)
    db.session.commit()

    print('Database seeded')

@app.cli.command('all_cards')
def all_cards():
    #select * from cards;
    #stmt = db.select(Card).limit(4)
    stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    #print(stmt)
    #need a variable for execute as need a vell to store the data/into
    #cards = db.session.execute(stmt)
    #cards = db.session.scalars(stmt) (for use with limit etc)
    cards = db.session.scalars(stmt) #for use with where... because filtering out from all
    #iterate over scalars
    for card in cards:
       # print(card)
        #print(card.__dict__)
        print(card.title)
        # print(card.description)
        # print(card.date_created)
    #this just returns an object in which data is housed
    #print(cards)
    #this returns a list of tuples
    #print(cards.all())

@app.route('/cards/')
def all_cards():
    #select * from cards;
    stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)
    # this goes with the to_dict workaround around marshmallow return [card.to_dict() for card in cards]


#create route index route to test server
@app.route('/')
def index():
    return 'Hello, world!'

#use flask run code here or in console below enter 'flask run' but then no debug on.
#Call with flask db_create```
