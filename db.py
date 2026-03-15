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
    sql = "SELECT id, codename, hardware_id FROM players WHERE id = %s"
    with get_conn() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(sql, (player_id,))
        return cur.fetchone()

# Will also be used to update player codename if it already exists
def insert_player(player_id: int, codename: str, hardware_id: int):
    with get_conn() as conn, conn.cursor() as cur:
        
        #Check if Id already exisits
        cur.execute("SELECT 1 FROM players WHERE id = %s", (player_id,))
        exists = cur.fetchone() is not None

        if exists:
            cur.execute(
                "UPDATE players SET codename = %s, hardware_id = %s WHERE id = %s",
                (codename, hardware_id, player_id),
            )
        else:
            cur.execute(
                "INSERT INTO players (id, codename, hardware_id) VALUES (%s, %s, %s)",
                (player_id, codename, hardware_id),
            )

        conn.commit()

#Creates a new column in the database for hardware_id 
#ensures that wherever the program is ran, the database will be correctly updated
def ensure_players_schema():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            ALTER TABLE players
            ADD COLUMN IF NOT EXISTS hardware_id INTEGER
        """)
        conn.commit()

#Used to make sure there are no duplicate hardware_ids
def fetch_player_by_hardware_id(hardware_id: int):
    sql = "SELECT id, codename, hardware_id FROM players WHERE hardware_id = %s"
    with get_conn() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(sql, (hardware_id,))
        return cur.fetchone()


