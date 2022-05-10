from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from models.provider import Provider
from flask import Flask, render_template, url_for, request, redirect


#additional imports
from config import SQLALCHEMY_DATABASE_URI
from importProviders import import_providers
from seed_database import seed

app = Flask(__name__)
#app.debug=True

engine = db.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
s= Session()

def main():
    #connect to database
    s = Session()
    s.close()

@app.route('/')
def index():
    return render_template('index.html')
 .
@app.route('/providers', methods=['GET'])
def getProviders():
    get_provider = s.query(Provider.first_name, Provider.last_name, Provider.rating).order_by(Provider.rating.desc()).all()
    return render_template('providers.html', providers = get_provider)

@app.route('/providers/<isactive>', methods=['GET'])
def getActiveProviders(isactive):
    is_active = s.query(Provider.first_name, Provider.last_name, Provider.rating, Provider.active).filter_by(active=True).order_by(Provider.rating.desc()).all()
    return render_template('providers.html', providers = is_active)

@app.route('/isnotactive/<isnotactive>', methods=['GET'])
def getInactiveProviders(isnotactive):
    is_not_active = s.query(Provider.first_name, Provider.last_name, Provider.rating, Provider.active).filter_by(active=False).order_by(Provider.rating.desc()).all()
    return render_template('providers.html', providers = is_not_active)
'''

#filter by variety of traits
@app.route('/providerfilter/<filter>', methods=['GET'])
def filterProviders(filter):
    data = request.form
    val1 = data["val1"]
    val2 = data["val2"]
    subquery = s.query(Provider.first_name, Provider.last_name, Provider.sex, Provider.birth_date, Provider.rating, Provider.primary_skills, Provider.secondary_skill, Provider.company, Provider.active, Provider.country, Provider.language).contains(val1).subquery()
    filter_provider = s.query(Provider.first_name, Provider.last_name, Provider.sex, Provider.birth_date, Provider.rating, Provider.primary_skills, Provider.secondary_skill, Provider.company, Provider.active, Provider.country, Provider.language).contains(val2.in_(subquery))
    return render_template('providers.html', providers = filter_provider)

#add column and create trigger to count query responses, append column + 1

'''


if __name__ == "__main__":
    app.run()
