import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Manufacturer, Base, Software, User

now = datetime.datetime.now()

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(username="Bgates", password="bgates123",
             email="Billy@InsanelyRich.com", name="Bill Gates",
             picture="bgates.jpg")

session.add(User1)
session.commit()

User2 = User(username="ShantAdobe", password="shant543",
             email="Shantanu@adobe.com", name="Shantanu Narayen",
             picture="AdobeCEO.jpg")

session.add(User2)
session.commit()

User3 = User(username="AdamSel1", password="selinskyPop",
             email="AdamSel@tableau.com", name="Adam Selipsky",
             picture="TableauCEO.jpg")

session.add(User3)
session.commit()


# Manufacturer
manufacturer1 = Manufacturer(name="Microsoft", corporate_city="Seattle",
                             created_date=str(now), picture="mslogo.jpg",
                             user_id=1)

session.add(manufacturer1)
session.commit()

manufacturer2 = Manufacturer(name="Adobe", corporate_city="San Jose",
                             created_date=str(now),
                             picture="adobe.jpg", user_id=2)

session.add(manufacturer2)
session.commit()

manufacturer3 = Manufacturer(name="Tableau", corporate_city="Seattle",
                             created_date=str(now),
                             picture="tableau.png", user_id=3)

session.add(manufacturer3)
session.commit()

# Software
software1 = Software(name="Windows Movie Maker", price="$99.99",
                     year_published="2015", category="Media Editing",
                     created_date=str(now), manufacturer_id=1,
                     manufacturer=manufacturer1, user_id=1)

session.add(software1)
session.commit()

software2 = Software(name="Excel", price="$69.99", year_published="2016",
                     category="Data", manufacturer_id=1,
                     created_date=str(now),
                     manufacturer=manufacturer1, user_id=1)

session.add(software2)
session.commit()

software3 = Software(name="Power BI", price="$0.00", year_published="2017",
                     category="Visualization", created_date=str(now),
                     manufacturer_id=1, manufacturer=manufacturer1, user_id=1)

session.add(software3)
session.commit()

software4 = Software(name="Photoshop", price="$699.99", year_published="2018",
                     category="Media Editing", created_date=str(now),
                     manufacturer_id=2, manufacturer=manufacturer2, user_id=2)

session.add(software4)
session.commit()

software5 = Software(name="Premiere Editing", price="$399.99",
                     year_published="2018", category="Media Editing",
                     created_date=str(now), manufacturer_id=2,
                     manufacturer=manufacturer2, user_id=2)

session.add(software5)
session.commit()

software6 = Software(name="Tableau Visualization", price="$1099.99",
                     year_published="2018", category="Visualization",
                     created_date=str(now), manufacturer_id=3,
                     manufacturer=manufacturer3, user_id=3)

session.add(software6)
session.commit()

print ("added software!")
