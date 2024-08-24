import sqlite3


def jadwal(hari):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    print("Jadwal hari " + hari + ":")
    c.execute("SELECT * FROM jadwal WHERE hari=?", (hari,))
    rows = c.fetchall()
    mapel = []
    guru = []
    for n in rows:
        kode = (n[3],)
        c.execute("SELECT * FROM kodeguru WHERE id=?", kode)
        jadwal = c.fetchall()
        if jadwal:
            x = jadwal[0][2]
            y = jadwal[0][1]
            mapel.append(x)
            guru.append(y)
    conn.close()
    return mapel, guru


def get_information(name):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_information WHERE name=?", (name,))
    rows = c.fetchall()
    conn.close()
    return rows


def update_user_information(name, column, value):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute(f"UPDATE user_information SET {column} = ? WHERE name = ?", (value, name))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    info = get_information("Raja Iblis")
    for i in info:
        print(i)
