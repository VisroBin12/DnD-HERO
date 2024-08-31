import sqlalchemy as db

engine = db.create_engine('sqlite:///dnd.db')

conn = engine.connect()
metadata = db.MetaData()

spells =  db.Table(
    'spells', metadata,
    db.Column('spell_id', db.Integer, primary_key=True),
    db.Column('spell_name', db.Text),
    db.Column('spell_lvl', db.Integer),
    db.Column('spell_desc', db.Text),
    db.Column('spell_school', db.Text)
)
armor1 =  db.Table(
    'armor1', metadata,
    db.Column('items_id', db.Integer, primary_key=True),
    db.Column("items_subclass", db.Text),
    db.Column("items_name", db.Text),
    db.Column('items_cost', db.Integer),
    db.Column('items_kd', db.Integer),
    db.Column('items_power', db.Integer),
    db.Column('items_stealth', db.Integer),
    db.Column('items_weight', db.Integer)
)
items1 =  db.Table(
    'items1', metadata,
    db.Column('items_id', db.Integer, primary_key=True),
    db.Column("items_name", db.Text),
    db.Column("items_cost", db.Integer),
    db.Column('items_weight', db.Integer),
)
skills =  db.Table(
    'skills', metadata,
    db.Column('skills_id', db.Integer, primary_key=True),
    db.Column('skills_name', db.Text),
    db.Column('skills_desc', db.Text),
)
skills_peaceful =  db.Table(
    'skills_peaceful', metadata,
    db.Column('skills_id', db.Integer, primary_key=True),
    db.Column('skills_name', db.Text),
    db.Column('skills_price', db.Integer),
    db.Column('skills_desc', db.Text),
    db.Column('skills_class', db.Text)
    )
metadata.create_all(engine)

# insert_data = items_2.insert().values([{
#     'items_name': 'Алхимический огонь (фляга)',
#     'items_cost': '50',
#     'items_weight': '`1`',
# }])
# conn.execute(insert_data)
conn.commit()
# insert_data = armor1.insert().values([{
#     'items_subclass': 'Легкий доспех',
#     'items_name': 'Стёганый',
#     'items_cos': '5',
#     'items_kd': '12',
#     'items_power': '0',
#     'items_stealth': '1',
#     'items_weight': '8',
# }])


def get_spells():
    selection_query = db.select(spells)
    selection_result = conn.execute(selection_query)
    return selection_result.fetchall()

def get_skills():
    selection_query = db.select(skills)
    selection_result = conn.execute(selection_query)
    return selection_result.fetchall()

def get_skills_peaceful():
    selection_query = db.select(skills_peaceful)
    selection_result = conn.execute(selection_query)
    return selection_result.fetchall()

def get_items1():
    selection_query = db.select(items1)
    selection_result = conn.execute(selection_query)
    return selection_result.fetchall()    

def get_armor1():
    selection_query = db.select(armor1)
    selection_result = conn.execute(selection_query)
    return selection_result.fetchall()   

def create(form_data, table):
    if table == "spells":
        insert_data = spells.insert().values([{
            "spell_name": form_data["spell_name"],
            "spell_lvl": form_data["spell_lvl"],
            "spell_school": form_data["spell_school"],
            "spell_desc": form_data["spell_desc"]
        }])
        conn.execute(insert_data)
        conn.commit()
    elif table == "skills":
        insert_data = skills.insert().values([{
            "skill_name": form_data["skill_name"],
            "skill_desc": form_data["skill_desc"]
        }])
        conn.execute(insert_data)
        conn.commit()
    elif table == "skills_peaceful":
        insert_data = skills_peaceful.insert().values([{
            "skill_peaceful_name": form_data["skill_peaceful_name"],
            "skill_peaceful_price": form_data["skill_peaceful_price"],
            "skill_peaceful_desc": form_data["skill_peaceful_desc"],
            "skill_peaceful_class": form_data["skill_peaceful_class"]
        }])
        conn.execute(insert_data)
        conn.commit()
    elif table == "items1":
        insert_data = items1.insert().values([{
            "items1_name": form_data["items1_name"],
            "items1_cost": form_data["items1_cost"],
            "items1_weight": form_data["items1_weight"]
        }])
        conn.execute(insert_data)
        conn.commit()
    elif table == "armor1":
        insert_data = armor1.insert().values([{
            "armor1_subclass": form_data["armor1_subclass"],
            "armor1_name": form_data["armor1_name"],
            "armor1_cost": form_data["armor1_cost"],
            "armor1_kd": form_data["armor1_kd"],
            "armor1_power": form_data["armor1_power"],
            "armor1_stealth": form_data["armor1_stealth"],
            "armor1_weigth": form_data["armor1_weight"]
        }])
        conn.execute(insert_data)
        conn.commit()

    
    


# with engine.connect() as connection: 
#     result = connection.execute(db.text('ALTER TABLE skills DROP COLUMN skills_class'))

