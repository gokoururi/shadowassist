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
        Character(
            name="Professor Dr. Anluan Morris",
            type="pc",
            body=2,
            agility=2,
            reaction=2,
            strength=1,
            willpower=6,
            logic=3,
            intuition=3,
            charisma=7,
            edge=2,
            currentEdge=2,
            magic=7,
            essence=6,
            physDamage=0,
            stunDamage=0
        ),
        Skill(character_id=1, name="Alchemie",          level=8,    attribute="magic"),
        Specialization(skill_id=1,  name="Berührung"),
        Skill(character_id=1, name="Herbeirufen",       level=6,    attribute="magic"),
        Skill(character_id=1, name="Spruchzauberei",    level=6,    attribute="magic"),
        Skill(character_id=1, name="Arkana",            level=5,    attribute="logic"),
        Skill(character_id=1, name="Chemie",            level=4,    attribute="logic"),
        Skill(character_id=1, name="Wahrnehmung",       level=4,    attribute="intuition"),
        Specialization(skill_id=6, name="Sehen"),
        Specialization(skill_id=6, name="Hören"),
        Skill(character_id=1, name="Überreden",         level=2,    attribute="charisma"),
        Skill(character_id=1, name="Askennen",          level=1,    attribute="intuition"),
        Skill(character_id=1, name="Bodenfahrzeuge",    level=1,    attribute="reaction"),
        Skill(character_id=1, name="Erste Hilfe",       level=1,    attribute="logic"),
        Skill(character_id=1, name="Klingenwaffen",     level=1,    attribute="agility"),
        Skill(character_id=1, name="Pistolen",          level=1,    attribute="agility"),
        Skill(character_id=1, name="Ritualzauberei",    level=1,    attribute="magic"),
        Skill(character_id=1, name="Verkleiden",        level=1,    attribute="intuition"),
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
