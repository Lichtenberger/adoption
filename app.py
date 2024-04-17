from flask import Flask, request, redirect, render_template, flash, url_for, jsonify
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'itwouldntbesecretifitoldyou'

connect_db(app)
db.create_all()

@app.route('/')
def pets_list():
    '''page showing list of pets'''

    pets = Pet.query.all()

    render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''add a pet '''

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} has been added')
        return redirect(url_for('list_pets'))

    else:
        return render_template('pet_add_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    '''edit pet profile'''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f'{pet.name} has been updated')
        return redirect(url_for('list_pets'))
    
    else:
        return render_template('pet_edit_form', form=form, pet=pet)
    
@app.route('/api/pets/<int:pet_id>', methods=['GET'])
def api_get_pet(pet_id):
    '''return json about pet'''

    pet = Pet.query.get_or_404(pet_id)
    info = {'name': pet.name, 'age': pet.age}

    return jsonify(info)