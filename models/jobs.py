import database

def create_job(shipper_id, type, weight, pick_up, drop_off, suburb, state):
    database.create(
        "INSERT INTO jobs (shipper_id, type, weight, pick_up, drop_off, suburb, state)VALUES (%s,%s,%s,%s,%s,%s,%s)",
        [shipper_id, type, weight, pick_up, drop_off, suburb, state]
    )