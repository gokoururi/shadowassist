from shadowassist import db
from sqlalchemy.ext.associationproxy import association_proxy

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

    cas = db.relationship("CharacterAttributes", backref="character")
    attributes = association_proxy("cas", "attribute")


class CharacterAttributes(db.Model):
    __tablename__ = 'character_attributes'
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'))
    level = db.Column(db.Integer)

    #attribute = db.relationship("Attribute", backref="CharacterAttributes")

class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    displayName = db.Column(db.String(10))
    displayNameShort = db.Column(db.String(5))
    cas = db.relationship("CharacterAttributes", backref="attribute")
    level = association_proxy("cas", "level")
#    characters = db.relationship("CharacterAttributes", primaryjoin=id == CharacterAttributes.attribute_id)


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
