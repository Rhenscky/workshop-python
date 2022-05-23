# Flask

Flask adalah sebuah web framework yang ditulis dengan bahasa Python dan tergolong sebagai jenis microframework. Flask
berfungsi sebagai kerangka kerja aplikasi dan tampilan dari suatu web. Dengan menggunakan Flask dan bahasa Python, pengembang dapat membuat sebuah web yang terstruktur dan dapat mengatur behaviour suatu web dengan lebih mudah.

Flask bergantung pada mesin template `Jinja` dan toolkit `WSGI Werkzeug`. Dokumentasi untuk perpustakaan ini dapat ditemukan di:
 * Dokumentasi Jinja

Jinja adalah mesin templating yang cepat, ekspresif, dan dapat diperluas. Placeholder khusus dalam template memungkinkan penulisan kode yang mirip dengan sintaks Python. Kemudian template dilewatkan data untuk membuat dokumen akhir.

**Instalasi**
Jinja mendukung Python 3.7 dan yang lebih baru. Kami juga merekomendasikan penggunaan lingkungan virtual untuk mengisolasi dependensi proyek Anda dari proyek lain dan sistem.

Instal versi Jinja terbaru menggunakan pip:

```python
$ pip install Jinja2
```
Dependensi

Ini akan diinstal secara otomatis saat menginstal Jinja.
 - MarkupSafe lolos dari input yang tidak tepercaya saat merender template untuk menghindari serangan injeksi.

Dependensi Opsional
 - Distribusi ini tidak akan diinstal secara otomatis.

Babel menyediakan dukungan terjemahan dalam template.

 * Dokumentasi Werkzeug

werkzeug kata benda Jerman: "alat". Etimologi: werk ("pekerjaan"), zeug ("barang")

Werkzeug adalah perpustakaan aplikasi web WSGI yang komprehensif. Ini dimulai sebagai kumpulan sederhana dari berbagai utilitas untuk aplikasi WSGI dan telah menjadi salah satu perpustakaan utilitas WSGI paling canggih.

Werkzeug tidak memberlakukan dependensi apa pun. Terserah pengembang untuk memilih mesin template, adaptor database, dan bahkan bagaimana menangani permintaan.

## User Guide

Bagian dokumentasi ini, yang sebagian besar berbentuk prosa, dimulai dengan beberapa informasi latar belakang tentang Flask, kemudian berfokus pada petunjuk langkah demi langkah untuk pengembangan web dengan Flask.

**Foreword**

Baca ini sebelum Anda mulai menggunakan Flask. Mudah-mudahan ini menjawab beberapa pertanyaan tentang maksud dan tujuan proyek, dan kapan Anda harus atau tidak menggunakannya.

**Apa yang dimaksud dengan "mikro"?**

"Mikro" tidak berarti bahwa seluruh aplikasi web Anda harus masuk ke dalam satu file Python (walaupun tentu saja bisa), juga tidak berarti bahwa Flask tidak memiliki fungsionalitas. "Mikro" dalam kerangka mikro berarti Flask bertujuan untuk menjaga inti tetap sederhana namun dapat diperluas. Flask tidak akan membuat banyak keputusan untuk Anda, seperti database apa yang akan digunakan. Keputusan yang dibuatnya, seperti mesin templating apa yang digunakan, mudah diubah. Segala sesuatu yang lain terserah Anda, sehingga Flask bisa menjadi semua yang Anda butuhkan dan tidak ada yang tidak Anda butuhkan.

**Konfigurasi dan Konvensi**

Flask memiliki banyak nilai konfigurasi, dengan default yang masuk akal, dan beberapa konvensi saat memulai. Dengan konvensi, template dan file statis disimpan dalam subdirektori di dalam pohon sumber Python aplikasi, dengan nama templatesdan masing- static masing. Meskipun ini dapat diubah, Anda biasanya tidak perlu melakukannya, terutama saat memulai.

**Tumbuh dengan Flask**
Saat basis kode Anda tumbuh, Anda bebas membuat keputusan desain yang sesuai untuk proyek Anda. Flask akan terus memberikan lapisan lem yang sangat sederhana untuk yang terbaik yang ditawarkan Python. Anda dapat menerapkan pola lanjutan di SQLAlchemy atau alat database lain, memperkenalkan persistensi data non-relasional yang sesuai, dan memanfaatkan alat kerangka-agnostik yang dibuat untuk WSGI, antarmuka web Python.

## Installation

**Python Version**

Kami merekomendasikan menggunakan versi terbaru dari Python. Flask mendukung Python 3.7 dan yang lebih baru.

**Dependencies**

Distribusi ini akan diinstal secara otomatis saat menginstal Flask.
 - Werkzeug mengimplementasikan WSGI, antarmuka Python standar antara aplikasi dan server.
 - Jinja adalah bahasa template yang merender halaman yang dilayani aplikasi Anda.
 - MarkupSafe hadir dengan Jinja. Itu lolos dari input yang tidak tepercaya saat merender template untuk menghindari serangan injeksi.
 - ItsDangerous menandatangani data dengan aman untuk memastikan integritasnya. Ini digunakan untuk melindungi cookie sesi Flask.
 - Klik adalah kerangka kerja untuk menulis aplikasi baris perintah. Ini memberikan flaskperintah dan memungkinkan menambahkan perintah manajemen kustom.

**Optional dependencies**

Distribusi ini tidak akan diinstal secara otomatis. Flask akan mendeteksi dan menggunakannya jika Anda menginstalnya.
 - Blinker menyediakan dukungan untuk Sinyal .
 - python-dotenv mengaktifkan dukungan untuk Variabel Lingkungan Dari dotenv saat menjalankan flask perintah.
 - Watchdog menyediakan reloader yang lebih cepat dan efisien untuk server pengembangan.

**greenlet**

Anda dapat memilih untuk menggunakan gevent atau eventlet dengan aplikasi Anda. Dalam hal ini, diperlukan greenlet>=1.0. Saat menggunakan PyPy, PyPy>=7.3.7 diperlukan.
Ini bukan versi minimum yang didukung, mereka hanya menunjukkan versi pertama yang menambahkan fitur yang diperlukan. Anda harus menggunakan versi terbaru dari masing-masing.

**Virtual environments**

Gunakan lingkungan virtual untuk mengelola dependensi untuk proyek Anda, baik dalam pengembangan maupun produksi.
Masalah apa yang dipecahkan oleh lingkungan virtual? Semakin banyak proyek Python yang Anda miliki, semakin besar kemungkinan Anda perlu bekerja dengan berbagai versi pustaka Python, atau bahkan Python itu sendiri. Versi pustaka yang lebih baru untuk satu proyek dapat merusak kompatibilitas di proyek lain.
Lingkungan virtual adalah grup independen dari pustaka Python, satu untuk setiap proyek. Paket yang diinstal untuk satu proyek tidak akan memengaruhi proyek lain atau paket sistem operasi.
Python dibundel dengan venv modul untuk membuat lingkungan virtual.

**Create an environment**
Buat folder proyek dan venv folder di dalam:

```python
> mkdir myproject
> cd myproject
> py -3 -m venv venv
```

**Activate the environment**

```python
> venv\Scripts\activate
```

**Install Flask**

```python
$ pip install Flask
```

# Quickstart

Ingin memulai? Halaman ini memberikan pengenalan yang baik untuk Flask. Ikuti Instalasi untuk menyiapkan proyek dan menginstal Flask terlebih dahulu.

## A Minimal Application

Aplikasi Flask minimal terlihat seperti ini:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Jadi apa yang dilakukan kode itu?

1. Pertama kita mengimpor Flask kelas. Sebuah instance dari kelas ini akan menjadi aplikasi WSGI kami.
2. Selanjutnya kita membuat sebuah instance dari kelas ini. Argumen pertama adalah nama modul atau paket aplikasi. __name__adalah jalan pintas yang nyaman untuk ini yang sesuai untuk kebanyakan kasus. Ini diperlukan agar Flask tahu di mana mencari sumber daya seperti template dan file statis.
3. Kami kemudian menggunakan route()dekorator untuk memberi tahu Flask URL apa yang harus memicu fungsi kami.
4. Fungsi mengembalikan pesan yang ingin kita tampilkan di browser pengguna. Tipe konten default adalah HTML, jadi HTML dalam string akan dirender oleh browser.

Simpan sebagai hello.py atau yang serupa. Pastikan untuk tidak memanggil aplikasi Anda flask.pykarena ini akan bertentangan dengan Flask itu sendiri.

Untuk menjalankan aplikasi, gunakan perintah flask atau python -m flask . Sebelum Anda dapat melakukannya, Anda perlu memberi tahu terminal Anda aplikasi yang akan digunakan dengan mengekspor FLASK_APP variabel lingkungan:

```python
> set FLASK_APP=hello
> flask run
 * Running on http://127.0.0.1:5000/
```

# Tutorial

## Project Layout

Buat direktori proyek dan masukkan:

```python
$ mkdir flask-tutorial
$ cd flask-tutorial
```

Kemudian ikuti petunjuk instalasi untuk menyiapkan lingkungan virtual Python dan menginstal Flask untuk proyek Anda.

Tutorial akan menganggap Anda bekerja dari flask-tutorial direktori mulai sekarang. Nama file di bagian atas setiap blok kode relatif terhadap direktori ini.

Aplikasi Flask bisa sesederhana satu file.

`hello.py`

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

Namun, ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan paket untuk mengatur kode menjadi beberapa modul yang dapat diimpor jika diperlukan, dan tutorial ini juga akan melakukannya.

Direktori proyek akan berisi:
 * flaskr/, paket Python yang berisi kode aplikasi dan file Anda.
 * tests/, direktori yang berisi modul pengujian.
 * venv/, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.
 * File instalasi memberi tahu Python cara menginstal proyek Anda.
 * Konfigurasi kontrol versi, seperti git . Anda harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek Anda, berapa pun ukurannya.
* File proyek lain yang mungkin Anda tambahkan di masa mendatang.

Pada akhirnya, tata letak proyek Anda akan terlihat seperti ini:

```python
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

Jika Anda menggunakan kontrol versi, file berikut yang dihasilkan saat menjalankan proyek Anda harus diabaikan. Mungkin ada file lain berdasarkan editor yang Anda gunakan. Secara umum, abaikan file yang tidak Anda tulis. Misalnya, dengan git:

`.gitignore`

```python
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```

## Application Setup

Aplikasi Flask adalah turunan dari Flask kelas. Segala sesuatu tentang aplikasi, seperti konfigurasi dan URL, akan didaftarkan dengan kelas ini.

## The Application Factory

Saatnya untuk memulai pengkodean! Buat flaskr direktori dan tambahkan __init__.pyfile. Melayani tugas ganda : __init__.py itu akan berisi pabrik aplikasi, dan memberitahu Python bahwa flaskr direktori harus diperlakukan sebagai sebuah paket.

```python
$ mkdir flaskr
```

`flaskr/__init__.py`

```python
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

## Run The Application

Mode pengembangan menampilkan debugger interaktif setiap kali halaman memunculkan pengecualian, dan memulai ulang server setiap kali Anda membuat perubahan pada kode. Anda dapat membiarkannya berjalan dan hanya memuat ulang halaman browser saat Anda mengikuti tutorial.

```python
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

Anda akan melihat output yang mirip dengan ini:

```python
* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```

Kunjungi http://127.0.0.1:5000/hello di browser dan Anda akan melihat "Halo, Dunia!" pesan. Selamat, Anda sekarang menjalankan aplikasi web Flask Anda!

Jika program lain sudah menggunakan port 5000, Anda akan melihat atau saat server mencoba memulai. Lihat Alamat sudah digunakan untuk cara menanganinya. `Error: [Errno 98]OSError: [WinError 10013]`

## Define and Access the Database

Aplikasi akan menggunakan database SQLite untuk menyimpan pengguna dan posting. Python hadir dengan dukungan bawaan untuk SQLite dalam sqlite3 modul.

**Connect to the Database**

Hal pertama yang harus dilakukan ketika bekerja dengan database SQLite (dan sebagian besar perpustakaan database Python lainnya) adalah membuat koneksi ke sana. Setiap kueri dan operasi dilakukan menggunakan koneksi, yang ditutup setelah pekerjaan selesai.

Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan. Itu dibuat di beberapa titik saat menangani permintaan, dan ditutup sebelum respons dikirim.

`flaskr/db.py`

```python
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```

**Create the Tables**

Dalam SQLite, data disimpan dalam tabel dan kolom . Ini perlu dibuat sebelum Anda dapat menyimpan dan mengambil data. Flaskr akan menyimpan pengguna di usertabel, dan posting di posttabel. Buat file dengan perintah SQL yang diperlukan untuk membuat tabel kosong:

`flaskr/schema.sql`

```sql
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

Tambahkan fungsi Python yang akan menjalankan perintah SQL ini ke db.py file:

`flaskr/db.py`

```python
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```

**Register with the Application**

Fungsi close_dband init_db_command harus didaftarkan pada instance aplikasi; jika tidak, mereka tidak akan digunakan oleh aplikasi. Namun, karena Anda menggunakan fungsi pabrik, instans tersebut tidak tersedia saat menulis fungsi. Sebagai gantinya, tulis fungsi yang mengambil aplikasi dan melakukan pendaftaran.

`flaskr/db.py`

```python
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

`flaskr/__init__.py`

```python
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

**Initialize the Database File**

Sekarang setelah init-db terdaftar dengan aplikasi, itu dapat dipanggil menggunakan flask perintah, mirip dengan run perintah dari halaman sebelumnya.

Jalankan `init-db` perintah:

```python
$ flask init-db
Initialized the database.
```

## Blueprints and Views

Fungsi tampilan adalah kode yang Anda tulis untuk menanggapi permintaan ke aplikasi Anda. Flask menggunakan pola untuk mencocokkan URL permintaan yang masuk dengan tampilan yang seharusnya menanganinya. Tampilan mengembalikan data yang diubah Flask menjadi respons keluar. Flask juga bisa pergi ke arah lain dan menghasilkan URL ke tampilan berdasarkan nama dan argumennya.

**Create a Blueprint**

Blueprint adalah cara untuk mengatur sekelompok tampilan terkait dan kode lainnya. Daripada mendaftarkan tampilan dan kode lain secara langsung dengan aplikasi, mereka terdaftar dengan cetak biru. Kemudian cetak biru didaftarkan dengan aplikasi ketika tersedia di fungsi pabrik.

`flaskr/auth.py`

```python
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```

Ini menciptakan Blueprintbernama 'auth'. Seperti objek aplikasi, cetak biru perlu tahu di mana itu didefinisikan, sehingga __name__ diteruskan sebagai argumen kedua. Itu url_prefix akan ditambahkan ke semua URL yang terkait dengan cetak biru.

Impor dan daftarkan cetak biru dari pabrik menggunakan app.register_blueprint(). Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

`flaskr/__init__.py`

```python
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```

**The First View: Register**

Saat pengguna mengunjungi /auth/registerURL, register tampilan akan mengembalikan HTML dengan formulir untuk mereka isi. Ketika mereka mengirimkan formulir, itu akan memvalidasi input mereka dan menampilkan formulir lagi dengan pesan kesalahan atau membuat pengguna baru dan pergi ke halaman login.

`flaskr/auth.py`

```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```

**Login**

Tampilan ini mengikuti pola yang sama seperti register tampilan di atas.

`flaskr/auth.py`

```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```

Sekarang setelah pengguna id disimpan di session, itu akan tersedia pada permintaan berikutnya. Di awal setiap permintaan, jika pengguna login, informasi mereka harus dimuat dan tersedia untuk tampilan lain.

`flaskr/auth.py`

```python
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```

**Logout**

`flaskr/auth.py`

```python
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

**Require Authentication in Other Views**

Membuat, mengedit, dan menghapus posting blog akan membutuhkan pengguna untuk masuk. Seorang dekorator dapat digunakan untuk memeriksa ini untuk setiap tampilan yang diterapkannya.

`flaskr/auth.py`

```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```

**Endpoints and URLs**

Fungsi url_for() menghasilkan URL ke tampilan berdasarkan nama dan argumen. Nama yang terkait dengan tampilan juga disebut titik akhir , dan secara default sama dengan nama fungsi tampilan.

## Templates

Anda telah menulis tampilan autentikasi untuk aplikasi Anda, tetapi jika Anda menjalankan server dan mencoba membuka salah satu URL, Anda akan melihat TemplateNotFound kesalahan. Itu karena tampilan memanggil render_template(), tetapi Anda belum menulis template. File template akan disimpan di templates direktori di dalam flaskr paket.

Template adalah file yang berisi data statis serta placeholder untuk data dinamis. Sebuah template diberikan dengan data tertentu untuk menghasilkan dokumen akhir. Flask menggunakan perpustakaan template Jinja untuk merender template.

**The Base Layout**

Setiap halaman dalam aplikasi akan memiliki tata letak dasar yang sama di sekitar badan yang berbeda. Alih-alih menulis seluruh struktur HTML di setiap template, setiap template akan memperluas template dasar dan menimpa bagian tertentu.

`flaskr/templates/base.html`

```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```

**Register**

`flaskr/templates/auth/register.html`

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

**Log In**

`flaskr/templates/auth/login.html`

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```

**Register A User**

Sekarang setelah template otentikasi ditulis, Anda dapat mendaftarkan pengguna. Pastikan server masih berjalan ( jika tidak), lalu buka http://127.0.0.1:5000/auth/register .`flask run`

Tampilan dan template autentikasi berfungsi, tetapi saat ini terlihat sangat sederhana. Beberapa CSS dapat ditambahkan untuk menambahkan gaya ke tata letak HTML yang Anda buat. Gaya tidak akan berubah, jadi ini adalah file statis, bukan template.

Flask secara otomatis menambahkan statictampilan yang mengambil jalur relatif ke `flaskr/static` direktori dan menyajikannya. Template base.html sudah memiliki tautan ke style.css file:

```python
{{ url_for('static', filename='style.css') }}
```

Selain CSS, jenis file statis lainnya mungkin file dengan fungsi JavaScript, atau gambar logo. Mereka semua ditempatkan di bawah flaskr/static direktori dan direferensikan dengan .url_for('static', filename='...')

Tutorial ini tidak berfokus pada cara menulis CSS, jadi Anda cukup menyalin yang berikut ke dalam flaskr/static/style.css file:

`flaskr/static/style.css`

```css
html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
nav h1 { flex: auto; margin: 0; }
nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
.content { padding: 0 1rem 1rem; }
.content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
.content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
.flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
.post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
.post > header > div:first-of-type { flex: auto; }
.post > header h1 { font-size: 1.5em; margin-bottom: 0; }
.post .about { color: slategray; font-style: italic; }
.post .body { white-space: pre-line; }
.content:last-child { margin-bottom: 0; }
.content form { margin: 1em 0; display: flex; flex-direction: column; }
.content label { font-weight: bold; margin-bottom: 0.5em; }
.content input, .content textarea { margin-bottom: 1em; }
.content textarea { min-height: 12em; resize: vertical; }
input.danger { color: #cc2f2e; }
input[type=submit] { align-self: start; min-width: 10em; }
```

## Blog Blueprint

Kita akan menggunakan teknik yang sama yang Kita pelajari saat menulis cetak biru otentikasi untuk menulis cetak biru blog. Blog harus mencantumkan semua posting, mengizinkan pengguna yang masuk untuk membuat posting, dan mengizinkan penulis posting untuk mengedit atau menghapusnya.

**The Blueprint**

Tentukan cetak biru dan daftarkan di pabrik aplikasi.

`flaskr/blog.py`

```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```

Impor dan daftarkan cetak biru dari pabrik menggunakan `app.register_blueprint()`. Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

`flaskr/__init__.py`

```python
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```

**Index**

Indeks akan menampilkan semua posting, yang terbaru terlebih dahulu. `A JOIN` digunakan agar informasi penulis dari user tabel tersedia di hasil.

`flaskr/blog.py`

```python
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

`flaskr/templates/blog/index.html`

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```

Saat pengguna masuk, `header` blok menambahkan tautan ke `create` tampilan. Saat pengguna adalah penulis postingan, mereka akan melihat tautan “Edit” ke `update` tampilan postingan tersebut. `loop.last` adalah variabel khusus yang tersedia di dalam `Jinja` untuk loop . Ini digunakan untuk menampilkan baris setelah setiap posting kecuali yang terakhir, untuk memisahkannya secara visual.

**Create**

Tampilan createberfungsi sama dengan `register` tampilan auth. Baik formulir ditampilkan, atau data yang diposting divalidasi dan postingan ditambahkan ke database atau kesalahan ditampilkan.

```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

`flaskr/templates/blog/create.html`

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
{% endblock %}
```

**Update**

Baik tampilan `update` maupun `delete` tampilan perlu diambil post oleh iddan memeriksa apakah pembuatnya cocok dengan pengguna yang masuk. Untuk menghindari duplikasi kode, Anda dapat menulis fungsi untuk mendapatkan `post` dan memanggilnya dari setiap tampilan.

`flaskr/blog.py`

```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```

`abort()` akan memunculkan pengecualian khusus yang mengembalikan kode status `HTTP`. Dibutuhkan pesan opsional untuk ditampilkan dengan kesalahan, jika tidak, pesan default akan digunakan. `404` berarti “Tidak Ditemukan”, dan `403` berarti “Terlarang”. ( `401` berarti "Tidak Sah", tetapi Anda mengarahkan ulang ke halaman login alih-alih mengembalikan status itu.)

Argumen `check_author` didefinisikan sehingga fungsi dapat digunakan untuk mendapatkan a `post` tanpa memeriksa pembuatnya. Ini akan berguna jika Anda menulis tampilan untuk menampilkan kiriman individual pada halaman, di mana pengguna tidak masalah karena mereka tidak mengubah kiriman.

`flaskr/blog.py`

```python
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```

`flaskr/templates/blog/update.html`

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
{% endblock %}
```

**Delete**

Tampilan hapus tidak memiliki template sendiri, tombol hapus adalah bagian dari `update.html` dan memposting ke `/<id>/deleteURL`. Karena tidak ada template, itu hanya akan menangani `POST` metode dan kemudian mengarahkan ulang ke `index` tampilan.

`flaskr/blog.py`

```python
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```

## Make the Project Installable

Membuat proyek Anda dapat diinstal berarti Anda dapat membuat file distribusi dan menginstalnya di lingkungan lain, sama seperti Anda menginstal Flask di lingkungan proyek Anda. Ini membuat penerapan proyek Anda sama dengan menginstal pustaka lain, jadi Anda menggunakan semua alat Python standar untuk mengelola semuanya.

Menginstal juga dilengkapi dengan manfaat lain yang mungkin tidak terlihat dari tutorial atau sebagai pengguna Python baru, termasuk:
 * Saat ini, Python dan Flask memahami cara menggunakan flaskr paket hanya karena Anda menjalankan dari direktori proyek Anda. Menginstal berarti Anda dapat mengimpornya dari mana pun Anda menjalankannya.
 * Anda dapat mengelola dependensi proyek Anda seperti halnya paket lain, jadi instal.pip install `yourproject.whl`
 * Alat pengujian dapat mengisolasi lingkungan pengujian Anda dari lingkungan pengembangan Anda.

`Catatan: Ini diperkenalkan di akhir tutorial, tetapi dalam proyek masa depan Anda, Anda harus selalu memulai dengan ini.`

**Describe the Project**

File `setup.py` menjelaskan proyek Anda dan file miliknya.

`setup.py`

```python
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```

`packages` memberi tahu Python direktori paket apa (dan file Python yang dikandungnya) untuk disertakan. `find_packages()` menemukan direktori ini secara otomatis sehingga Anda tidak perlu mengetiknya. Untuk menyertakan file lain, seperti direktori statis dan template, `include_package_data` sudah diatur. Python membutuhkan file lain bernama `MANIFEST.in` untuk memberi tahu apa data lain ini.

`MANIFEST.in`

```python
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

Ini memberitahu Python untuk menyalin semua yang ada di direktori and, dan staticfile , tetapi untuk mengecualikan semua file `bytecode.templatesschema.sql`

**Install the Project**

Gunakan `pip` untuk menginstal proyek kita di lingkungan virtual.

Ini memberitahu pip untuk menemukan setup.pydi direktori saat ini dan menginstalnya dalam mode yang dapat diedit atau pengembangan. Mode yang dapat diedit berarti bahwa saat kita membuat perubahan pada kode lokal, Anda hanya perlu menginstal ulang jika Anda mengubah metadata tentang proyek, seperti dependensinya.

Anda dapat mengamati bahwa proyek tersebut sekarang diinstal dengan `.pip list`

```python
$ pip list

Package        Version   Location
-------------- --------- ----------------------------------
click          6.7
Flask          1.0
flaskr         1.0.0     /home/user/Projects/flask-tutorial
itsdangerous   0.24
Jinja2         2.10
MarkupSafe     1.0
pip            9.0.3
setuptools     39.0.1
Werkzeug       0.14.1
wheel          0.30.0
```

Tidak ada yang berubah dari cara Anda menjalankan proyek sejauh ini. `FLASK_APP` masih disetel ke flaskrdan masih menjalankan aplikasi, tetapi Anda dapat memanggilnya dari mana saja, bukan hanya `direktori.flask` `runflask-tutorial`

## Test Coverage

Menulis pengujian unit untuk aplikasi Anda memungkinkan Anda memeriksa apakah kode yang Anda tulis berfungsi seperti yang Anda harapkan. Flask menyediakan klien uji yang mensimulasikan permintaan ke aplikasi dan mengembalikan data respons.

Anda harus menguji sebanyak mungkin kode Anda. Kode dalam fungsi hanya berjalan ketika fungsi dipanggil, dan kode di cabang, seperti if blok, hanya berjalan ketika kondisi terpenuhi. Anda ingin memastikan bahwa setiap fungsi diuji dengan data yang mencakup setiap cabang.

Semakin dekat Anda mencapai cakupan 100%, semakin nyaman Anda karena membuat perubahan tidak akan mengubah perilaku orang lain secara tiba-tiba. Namun, cakupan 100% tidak menjamin bahwa aplikasi Anda tidak memiliki bug. Secara khusus, itu tidak menguji bagaimana pengguna berinteraksi dengan aplikasi di browser. Meskipun demikian, cakupan pengujian merupakan alat penting untuk digunakan selama pengembangan.

Anda akan menggunakan pytest dan coverage untuk menguji dan mengukur kode Anda. Instal keduanya:

```python
$ pip install pytest coverage
```

**Setup and Fixtures**

Kode tes terletak di testsdirektori. Direktori ini berada di sebelah paket flaskr, bukan di dalamnya. File `tests/conftest.py` berisi fungsi pengaturan yang disebut perlengkapan yang akan digunakan setiap pengujian. Pengujian dalam modul Python yang dimulai dengan test_, dan setiap fungsi pengujian dalam modul tersebut juga dimulai dengan test_.

Setiap pengujian akan membuat file database sementara baru dan mengisi beberapa data yang akan digunakan dalam pengujian. Tulis file SQL untuk memasukkan data itu.

`tests/data.sql`

```sql
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```

Fixture app akan memanggil pabrik dan lolos test_config untuk mengonfigurasi aplikasi dan database untuk pengujian alih-alih menggunakan konfigurasi pengembangan lokal Kita.

`tests/conftest.py`

```python
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```

**Factory**

Tidak banyak yang bisa diuji tentang pabrik itu sendiri. Sebagian besar kode akan dieksekusi untuk setiap tes, jadi jika ada yang gagal, tes lain akan memperhatikan.

Satu-satunya perilaku yang dapat berubah adalah melewati konfigurasi pengujian. Jika konfigurasi tidak diteruskan, harus ada beberapa konfigurasi default, jika tidak, konfigurasi harus diganti.

`tests/test_factory.py`

```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

Anda menambahkan hellorute sebagai contoh saat menulis pabrik di awal tutorial. Ini mengembalikan "Halo, Dunia!", Jadi tes memeriksa apakah data respons cocok.

**Database**

Dalam konteks aplikasi, `get_db` harus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah konteksnya, koneksi harus ditutup.

`tests/test_db.py`

```python
import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```

Perintah `init-db` harus memanggil `init_db` fungsi dan mengeluarkan pesan.

`tests/test_db.py`

```python
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```

Tes ini menggunakan monkeypatchperlengkapan Pytest untuk mengganti `init_db` fungsi dengan yang mencatat bahwa itu telah dipanggil. Perlengkapan `runner` yang Anda tulis di atas digunakan untuk memanggil `init-db` perintah dengan nama.

