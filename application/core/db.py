from databases import Database

DB_USER='root'
DB_PASSWORD='NoteAtl23.'
DB_HOST='localhost'
DB_NAME='university'

db_conn_string = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)

database = Database(db_conn_string, min_size=5, max_size=20)