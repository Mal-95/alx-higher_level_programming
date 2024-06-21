#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

def list_cities(username, password, db_name):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    cities = session.query(City).order_by(City.id).all()
    
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    
    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_cities(username, password, db_name)
    else:
        print("Usage: ./list_cities.py <mysql_username> <mysql_password> <database_name>")

