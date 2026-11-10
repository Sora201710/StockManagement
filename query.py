import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5433,
    dbname="postgres",
    user="postgres",
    password="postgres"
)

try:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM Stocks LIMIT 10")
        for row in cur.fetchall():
            print(row)
finally:
    conn.close()
