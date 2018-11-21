from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os.path

dbPath = '/opt/data/shadowassist.db'
app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/shadowassist'
app.config['SECRET_KEY'] = '28302703de0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbPath
db = SQLAlchemy(app)

from shadowassist import routes

from shadowassist.models import *

if not os.path.isfile(dbPath):
    data = [
        Spell(name="Panzerung",                  type="Manipulationszauber", drain="-2", alchemical=True),
        Spell(name="Geckogang",                  type="Manipulationszauber", drain="-3", alchemical=True),
        Spell(name="Entzünden",                  type="Manipulationszauber", drain="-1", alchemical=True),
        Spell(name="Verbesserte Unsichtbarkeit", type="Illusionszauber",     drain="-1", alchemical=True),
        Spell(name="Feuerball",                  type="Kampfzauber",         drain="-1", alchemical=True),
        Spell(name="Eisspeer",                   type="Kampfzauber",         drain="-3", alchemical=True),
        Spell(name="Energieball",                type="Kampfzauber",         drain="0",  alchemical=False),
        Spell(name="Energieblitz",               type="Kampfzauber",         drain="-3", alchemical=False),
        Spell(name="Reflexe Steigern",           type="Heilzauber",          drain="0",  alchemical=True),
        Spell(name="Schmerzresistenz",           type="Heilzauber",          drain="-4", alchemical=True),
        Spell(name="Stabilisieren",              type="Heilzauber",          drain="-4", alchemical=True),
        Prep(spell_id=1, force=8, potency=3, bonus=2, container="Trank", trigger="Brührung", state=0),
        Prep(spell_id=1, force=8, potency=6, bonus=2, container="Trank", trigger="Brührung", state=0),
        Prep(spell_id=1, force=8, potency=1, bonus=2, container="Trank", trigger="Brührung", state=1),
        Prep(spell_id=1, force=8, potency=6, bonus=2, container="Trank", trigger="Brührung", state=0),
        Prep(spell_id=1, force=8, potency=6, bonus=2, container="Trank", trigger="Brührung", state=0),
        Prep(spell_id=9, force=8, potency=5, bonus=2, container="Trank", trigger="Brührung", state=2),
    ]
    db.create_all()
    db.session.add_all(data)
    db.session.commit()
