import sqlite3

def CreateTable(NameTable,rows):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute(f"CREATE TABLE {NameTable}{rows}")
        db.commit()
        print("Alright")
    except:
        print("Wrong DATA")
    finally:
        db.close()

def DropTable(NameTable):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"DROP TABLE {NameTable}")
    db.commit()
    db.close()
    print("Done")

def insert(values):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute("INSERT INTO users VALUES(?,?,?,?)",values)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

def getIDUser(email):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT uid FROM users WHERE email= '{email}'")
    (id,) = cr.fetchone()
    return id

def deleteUser(name):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute(f"DELETE FROM users WHERE name='{name}'")
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
        print("Alright")

def length(NameTable='users'):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT * FROM {NameTable}")
    l = len(cr.fetchall())
    db.close()
    return int(l)

def getAllData(NameTable='users'):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT * FROM {NameTable}")
    for row in cr.fetchall():
        print(row)

def verify(email,password=None):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    if password != None:
        cr.execute(f"SELECT email FROM users  WHERE email= '{email}' AND pass = '{password}'")
    else:
        cr.execute(f"SELECT email FROM users  WHERE email= '{email}'")
    
    length = len(cr.fetchall())

    if length > 0:
        return True
    return False

def getName(email):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT name FROM users  WHERE email= '{email}'")
    name = cr.fetchone()
    return name[0]

def isenroll(uid,cid):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT cid FROM enroll WHERE uid = {uid}")
    courses = cr.fetchall()
    ids = []
    for course in courses:
        (course,) = course
        ids.append(course)
    db.close()
    return cid in ids

def enroll(uid,cid):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute("INSERT INTO enroll VALUES (?,?)",(uid,cid))
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

def deleteEnroll(uid):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute(f"DELETE FROM enroll WHERE uid= {uid} ")
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

def verifyCode(code):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT code FROM promocode WHERE code= '{code}'")
    length = len(cr.fetchall())
    db.close()
    if length > 0:
        return True
    return False

def insertCode(code):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"INSERT INTO promocode VALUES('{code}')")
    db.commit()
    db.close()

def deleteCode(code):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"DELETE FROM promocode WHERE code='{code}'")
    db.commit()
    db.close()

def getPrice(Cname):
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT price FROM courses  WHERE name= '{Cname}'")
    price = cr.fetchone()
    return price[0]


