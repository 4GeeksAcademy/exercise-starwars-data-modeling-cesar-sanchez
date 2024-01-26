import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    email = Column(String(250) , nullable=True)
    password = Column(String(250) , nullable=True)
    
class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer , nullable=False)
    eye_color = Column(String(250) , nullable=False)
    hair_color = Column(String(250) , nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    lenght = Column(Integer, nullable=False)
    manufacturer = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), unique =True)
    person = relationship(Person)

      
class Favourite(Base):
    __tablename__ = 'favourite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_usuario= Column(Integer, ForeignKey('usuario.id'), nullable=True)
    id_person = Column(Integer, ForeignKey('person.id'), nullable=True)
    id_vehicle = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    id_planet= Column(Integer, ForeignKey('planet.id'), nullable=True)     

    def to_dict(self):
        return {}





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
