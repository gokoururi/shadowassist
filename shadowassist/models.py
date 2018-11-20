from shadowassist import db

class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    type = db.Column(db.String(60))
    drain = db.Column(db.Integer)
    alchemical = db.Column(db.Boolean)

class Prep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spell_id = db.Column(db.Integer, db.ForeignKey('spell.id'))
    force = db.Column(db.Integer)
    potency = db.Column(db.Integer)
    bonus = db.Column(db.Integer)
    container = db.Column(db.String(60))
    trigger = db.Column(db.String(60))
    state = db.Column(db.Integer)
