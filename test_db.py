from app.db.connections import get_connection

conn = get_connection()

if conn:
    print("DB Connected Successfully")
    conn.close()
else:
    print("DB Connection Failed")
