import psycopg2
from secret import DATABASE_PASSWORD

def open_connection():
    conn = psycopg2.connect(
        database = "telebotDB",
        host = "localhost",
        user = "postgres",
        password = DATABASE_PASSWORD,
        port = 5432
    )
    return conn


def close_connection(conn, cur):
    cur.close()
    conn.close()


def create_database():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(
        """
        create table if not exists users(
            user_id varchar(30) primary key,
            username varchar(100),
            first_name varchar(100),
            last_name varchar(100)
        );
        """
    )
    conn.commit()
    close_connection(conn, cur)


def add_user(chat):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(
        f"""
        insert into users values (
            '{str(chat.id)}',
            '{str(chat.username)}',
            '{str(chat.first_name)}',
            '{str(chat.last_name)}'
        );
        """
    )
    conn.commit()
    close_connection(conn, cur)
    
    return f"User added succesifully!"

def get_user(user_id):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""
                select * from users
                where user_id = '{user_id}' """)
    user = cur.fetchone()
    close_connection(conn, cur)
    if user:
        return True 
    return False
