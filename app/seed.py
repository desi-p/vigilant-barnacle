from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from providers import Provider

#additional imports
from config import SQLALCHEMY_DATABASE_URI
from importProviders import import_providers
from seed_database import seed

engine = db.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

def main():
    #connect to database
    #seed table in postgres with data
    def seed_table():
        Session = sessionmaker(bind=engine)
        s = Session()
        print('seed table')
        seed()
        s.close()

    seed_table()

if __name__ == "__main__":
    main()