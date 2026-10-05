"""Modul backend autentikasi Flask."""

import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    """Membuka koneksi ke database."""
    return sqlite3.connect("users.db")


@app.route("/login", methods=["GET"])
def login():
    """Memproses autentikasi pengguna."""
    username = request.args.get("username", "")
    password = request.args.get("password", "")

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return "Login berhasil"

    return "Login gagal"


@app.route("/health")
def health():
    """Menampilkan status aplikasi."""
    return "Aplikasi berjalan dengan baik."


if __name__ == "__main__":
    app.run(port=5000)
