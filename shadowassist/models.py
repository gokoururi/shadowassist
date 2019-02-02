from shadowassist import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm.collections import attribute_mapped_collection

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    type = db.Column(db.String(10))
    body = db.Column(db.Integer)
    agility = db.Column(db.Integer)
    reaction = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    willpower = db.Column(db.Integer)
    logic = db.Column(db.Integer)
    intuition = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    edge = db.Column(db.Integer)
    currentEdge = db.Column(db.Integer)
    magic = db.Column(db.Integer)
    essence = db.Column(db.Float)
    physDamage = db.Column(db.Integer)
    stunDamage = db.Column(db.Integer)
    skills = db.relationship('Skill', backref='character', lazy=True)
    attributes = db.relationship(
        "Attribute",
        secondary="character_attributes",
        backref="characters",
        collection_class=attribute_mapped_collection('name')
    )

class CharacterAttributes(db.Model):
    __tablename__ = 'character_attributes'
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)
    attribute_name = db.Column(db.Integer, db.ForeignKey('attribute.name'), primary_key=True)
    level = db.Column(db.Integer)

class Attribute(db.Model):
    name = db.Column(db.String(20), primary_key=True)
    displayName = db.Column(db.String(10))
    displayNameShort = db.Column(db.String(5))
    cas = db.relationship("CharacterAttributes")
    level = association_proxy("cas", "level")


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    name = db.Column(db.String(60))
    level = db.Column(db.Integer)
    attribute = db.Column(db.String(15))
    specializations = db.relationship('Specialization', backref='skill', lazy=True)

class Specialization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    name = db.Column(db.String(60))

class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    type = db.Column(db.String(60))
    drain = db.Column(db.Integer)
    alchemical = db.Column(db.Boolean)
    preps = db.relationship('Prep', backref='spell', lazy=True)

class Prep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spell_id = db.Column(db.Integer, db.ForeignKey('spell.id'))
    force = db.Column(db.Integer)
    potency = db.Column(db.Integer)
    bonus = db.Column(db.Integer)
    container = db.Column(db.String(60))
    trigger = db.Column(db.String(60))
    state = db.Column(db.Integer)
