from flask import render_template, url_for, flash, redirect, request, jsonify
from shadowassist import app, db
from shadowassist.models import *

@app.route("/character")
def character():
    link = [
        {
            'url': '#',
            'icon': 'bars',
        },
        {
            'url': '#',
            'icon': 'pencil-alt',
        },
    ]
    return render_template('character.html', **locals(), title="Character Sheet")


@app.route("/")
@app.route("/preps")
def preps():
    spells = Spell.query.all()
    preps = Prep.query.order_by(Prep.state.desc(), Prep.id.asc()).all()
    link = [
        {
            'url': '#',
            'icon': 'bars',
        },
        {
            'url': url_for('createPrepSelectSpell', _external=True),
            'icon': 'plus-circle',
        },
    ]
    return render_template('preps.html', **locals(), title="Präparate")

@app.route("/prepChange/state/<int:prep_id>/<int:state>")
def prepChangeState(prep_id, state):
    prep = Prep.query.filter(Prep.id == prep_id)
    prep.update({'state': state})
    db.session.commit()
    return jsonify({"result": "ok"})

@app.route("/prepChange/delete/<int:prep_id>")
def prepChangeDelete(prep_id):
    prep = Prep.query.filter(Prep.id == prep_id).delete()
    db.session.commit()
    return jsonify({"result": "ok"})

def getSpellTypes(spells):
    spellTypes = []
    for spell in spells:
        if spell.type not in spellTypes:
            spellTypes.append(spell.type)
    return spellTypes

@app.route("/createPrep")
def createPrepSelectSpell():
    spells = Spell.query.all()
    spellTypes = getSpellTypes(spells)
    link = [
        {
            'url': '#',
            'icon': 'bars',
        },
        {
            'url': url_for('preps', _external=True),
            'icon': 'times',
        },
    ]
    return render_template('createPrep/00_selectSpell.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>")
def createPrepSelectContainer(spell_id):
    spell = Spell.query.filter(Spell.id == spell_id).first()
    link = [
        {
            'url': url_for('createPrepSelectSpell', _external=True),
            'icon': 'chevron-left',
        },
        {
            'url': url_for('preps', _external=True),
            'icon': 'times',
        },
    ]
    return render_template('createPrep/01_selectContainer.html', **locals(), title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>")
def createPrepSelectTrigger(spell_id, container):
    link = [
        {
            'url': url_for('createPrepSelectContainer',
                           spell_id=spell_id,
                           _external=True),
            'icon': 'chevron-left',
        },
        {
            'url': url_for('preps', _external=True),
            'icon': 'times',
        },
    ]
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/02_selectTrigger.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>/<trigger>")
def createPrepSelectForce(spell_id, container, trigger):
    link = [
        {
            'url': url_for('createPrepSelectTrigger',
                           spell_id=spell_id,
                           container=container,
                           _external=True),
            'icon': 'chevron-left',
        },
        {
            'url': url_for('preps', _external=True),
            'icon': 'times',
        },
    ]
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/03_selectForce.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>/<trigger>/<int:force>")
def createPrepSelectPotency(spell_id, container, trigger, force):
    link = [
        {
            'url': url_for('createPrepSelectForce',
                           spell_id=spell_id,
                           container=container,
                           trigger=trigger,
                           _external=True),
            'icon': 'chevron-left',
        },
        {
            'url': url_for('preps', _external=True),
            'icon': 'times',
        },
    ]
    spell = Spell.query.filter(Spell.id == spell_id).first()
    return render_template('createPrep/04_selectPotency.html',
                           **locals(),
                           title="Präparat Herstellen")

@app.route("/createPrep/<int:spell_id>/<container>/<trigger>/<int:force>/<int:potency>")
def createPrepResistDrain(spell_id, container, trigger, force, potency):
    link = [
        {
            'url': url_for('createPrepSelectPotency',
                           spell_id=spell_id,
                           container=container,
                           trigger=trigger,
                           force=force,
                           _external=True),
            'icon': 'chevron-left',
        },
        {
            'url': url_for('preps', _external=True),
            'icon': 'times',
        },
    ]
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
    return redirect(url_for('preps', _external=True))
