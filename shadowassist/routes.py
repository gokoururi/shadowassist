from flask import render_template, url_for, flash, redirect, request, jsonify
from shadowassist import app, db
from shadowassist.models import *

@app.route("/")
@app.route("/home")
def home():
    spells = Spell.query.all()
    preps = Prep.query.order_by(Prep.state.desc(), Prep.id.asc()).all()
    return render_template('home.html', spells=spells, preps=preps, title="Präparate")

@app.route("/prepChangeState/<int:prep_id>/<int:state>")
def prepChangeState(prep_id, state):
    prep = Prep.query.filter(Prep.id == prep_id)
    prep.update({'state': state})
    db.session.commit()
    return jsonify({"result": "ok"})

@app.route("/prepDelete/<int:prep_id>")
def prepChange(prep_id):
    prep = Prep.query.filter(Prep.id == prep_id).delete()
    db.session.commit()
    return jsonify({"result": "ok"})

@app.route("/createPrep")
def createPrepSelectSpell():
    spells = Spell.query.all()
    spellTypes = []
    for spell in spells:
        if spell.type not in spellTypes:
            spellTypes.append(spell.type)

    return render_template('createPrep/00_selectSpell.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>")
def createPrepSelectContainer(spell_id):
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/01_selectContainer.html', spell=spell, title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>")
def createPrepSelectTrigger(spell_id, container):
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/02_selectTrigger.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>/<trigger>")
def createPrepSelectForce(spell_id, container, trigger):
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/03_selectForce.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>/<trigger>/<int:force>")
def createPrepSelectPotency(spell_id, container, trigger, force):
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/04_selectPotency.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>/<trigger>/<int:force>/<int:potency>")
def createPrepResistDrain(spell_id, container, trigger, force, potency):
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/05_resistDrain.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/create/<int:spell_id>/<container>/<trigger>/<int:force>/<int:potency>")
def createPrepCreate(spell_id, container, trigger, force, potency):
    newPrep = Prep(spell_id=spell_id,
                   container=container,
                   trigger=trigger,
                   force=int(force),
                   potency=int(potency),
                   bonus=2,
                   state=1)
    db.session.add(newPrep)
    db.session.commit()
    return redirect(url_for('home', _external=True))
