import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_conn():
    user = os.getenv("PGUSER") or os.getenv("USER") or "student"
    dbname = os.getenv("PGDATABASE") or "photon"

    # try TCP local host
    try:
        return psycopg2.connect(dbname=dbname, user=user, host="127.0.0.1")
    except Exception:
        pass

    # fallback unix socket
    return psycopg2.connect(dbname=dbname, user=user, host="/var/run/postgresql")


def fetch_player_by_id(player_id: int):
    sql = "SELECT id, codename FROM players WHERE id = %s"
    with get_conn() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(sql, (player_id,))
        return cur.fetchone()

# Will also be used to update player codename if it already exists
def insert_player(player_id: int, codename: str):
    with get_conn() as conn, conn.cursor() as cur:
        
        #Check if Id already exisits
        cur.execute("SELECT 1 FROM players WHERE id = %s", (player_id,))
        exists = cur.fetchone() is not None

        if exists:
            cur.execute(
                "UPDATE players SET codename = %s WHERE id = %s",
                (codename, player_id),
            )
        else:
            cur.execute(
                "INSERT INTO players (id, codename) VALUES (%s, %s)",
                (player_id, codename),
            )

        conn.commit()


