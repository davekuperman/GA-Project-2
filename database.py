import psycopg2
from psycopg2.extras import RealDictCursor

def create(query, params):
    conn = psycopg2.connect("dbname=frelper")
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

def select_one(query, params):
    conn = psycopg2.connect("dbname=frelper") 
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, params)
    result = cur.fetchone()
    return result
   
def select_many(query):
    conn = psycopg2.connect("dbname=frelper") 
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query)
    result = cur.fetchall()
    return result


def write(query, params):
    conn = psycopg2.connect("dbname=frelper")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()
    
