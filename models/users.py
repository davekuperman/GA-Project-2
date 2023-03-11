import database

def create_shipper(firstName,lastName, email, phoneNumber, companyName, password_hash):
    database.create(
        "INSERT INTO shippers (firstName,lastName, email, phoneNumber, companyName, password_hash) VALUES (%s, %s, %s, %s, %s, %s)",
        [firstName,lastName, email, phoneNumber, companyName, password_hash]
    )


def create_carrier(firstName,lastName, email, phoneNumber, companyName, password_hash, profile_pic):
    database.create(
        "INSERT INTO carriers (firstName,lastName, email, phoneNumber, companyName, password_hash, profile_pic) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        [firstName,lastName, email, phoneNumber, companyName, password_hash, profile_pic]
    )

def get_shipper_by_email(email):
    shipper = database.select_one('SELECT * FROM shippers WHERE email = %s',[email])
    return shipper

def get_carrier_by_email(email):
    carrier = database.select_one('SELECT * FROM carriers WHERE email = %s',[email])
    return carrier

def get_carrier_by_id(id):
    carrier = database.select_one('SELECT * FROM carriers WHERE id = %s',[id])
    return carrier

def update_carrier_profile(email, firstname, lastname, phonenumber, companyname, profile_pic):
    database.write('UPDATE carriers SET firstname = %s, lastname = %s, phonenumber = %s, companyname = %s, profile_pic = %s WHERE email = %s',
    [firstname, lastname, phonenumber, companyname, profile_pic, email]
    )

def delete_carrier_profile(email):
    database.write('DELETE FROM carriers  WHERE email = %s',
    [email]
    )

