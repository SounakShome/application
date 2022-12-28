from flask import Flask, render_template, request
import mysql.connector as sql

app = Flask(__name__)

def log_request(req: 'flask_request', res) -> None:
    conn = sql.connect(host = 'localhost', user = 'root', password = 'Sounak@#$2004', database = 'participants')
    cursor = conn.cursor()
    _SQL = "insert into log (first_name, last_name, dob, gender, country_code, phone_number, email, address, city, state, zip_code) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(_SQL, (req.form['first_name'],
                          req.form['last_name'],
                          req.form['dob'],
                          req.form['gender'],
                          req.form['country_code'],
                          req.form['phone_number'],
                          req.form['email'],
                          req.form['address'],
                          req.form['city'],
                          req.form['state'],
                          req.form['zip_code'],))
    cursor.execute("select max(id) from log;")
    data = cursor.fetchone()
    for x in data:
        global num
        num = x
    conn.commit()
    cursor.close()
    conn.close()

def edit_request(req: 'flask_request', res) -> None:
    conn = sql.connect(host = 'localhost', user = 'root', password = 'Sounak@#$2004', database = 'participants')
    cursor = conn.cursor()
    _SQL = "update log set first_name = %s, last_name = %s, dob = %s, gender = %s, country_code = %s, phone_number = %s, email = %s, address = %s, city = %s, state = %s, zip_code = %s where id = %s"
    cursor.execute(_SQL, (req.form['first_name'],
                          req.form['last_name'],
                          req.form['dob'],
                          req.form['gender'],
                          req.form['country_code'],
                          req.form['phone_number'],
                          req.form['email'],
                          req.form['address'],
                          req.form['city'],
                          req.form['state'],
                          req.form['zip_code']))
    conn.commit()
    cursor.close()
    conn.close()

def error():
    conn = sql.connect(host = 'localhost', user = 'root', password = 'Sounak@#$2004', database = 'participants')
    cursor = conn.cursor()
    cursor.execute("select email from log;")
    global emails
    emails = cursor.fetchall()
    global ids
    cursor.execute("select id from log;")
    ids = cursor.fetchall()
    return ids2
    return emails

def detail_request():
    conn = sql.connect(host = 'localhost', user = 'root', password = 'Sounak@#$2004', database = 'participants')
    cursor = conn.cursor()
    global num_id, name, first_name, last_name, dob, gender, country_code, phone_number, email, address, city, state, zip_code
    num = request.form['num1']
    email = request.form['email']
    _SQL = "select * from log where id = %s and email = %s;"
    cursor.execute(_SQL, (num,
                          email,))
    data = cursor.fetchone()
    num_id = data[0]
    first_name = data[1]
    last_name = data[2]
    name = data[1]+" "+data[2]
    dob = data[3]
    gender = data[4]
    country_code = data[5]
    phone_number = data[6]
    email = data[7]
    address = data[8]
    city = data[9]
    state = data[10]
    zip_code = data[11]
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/confirm', methods=['POST'])
def check() -> 'html':
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    gender = request.form['gender']
    countrycode = request.form['country_code']
    phone_number = request.form['phone_number']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    title = "Application Form"
    return render_template('confirm.html',
                            the_first_name = first_name,
                            the_last_name = last_name,
                            the_dob = dob,
                            the_gender = gender,
                            the_country_code = countrycode,
                            the_phone_number = phone_number,
                            the_email = email,
                            the_address = address,
                            the_city = city,
                            the_state = state,
                            the_zip_code = zip_code,
                            the_title = title,)

@app.route('/submitted', methods=['POST'])
def ok() -> 'html':
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    gender = request.form['gender']
    country_code = request.form['country_code']
    phone_number = request.form['phone_number']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    result = {first_name, last_name, dob, gender, phone_number, email, address, city, state, zip_code}
    results = str(result)
    log_request(request, results)
    return render_template('submitted.html',
                            id = num,)

@app.route('/')
@app.route('/', methods=['POST'])
def index() -> 'html':
    return render_template('index.html')

@app.route('/application', methods=['POST'])
def entry_page() -> 'html':
    return render_template('form.html', the_title = "Application Form")

@app.route('/e1', methods=['POST'])
def e1() -> 'html':
    return render_template('e1.html')

@app.route('/e2', methods=['POST'])
def e2() -> 'html':
    return render_template('e2.html')

@app.route('/details', methods=['POST'])
def details() -> 'html':
    detail_request()
    return render_template('details.html',
                           the_id = num_id,
                           the_name = name,
                           the_dob = dob,
                           the_gender = gender,
                           the_country_code = country_code,
                           the_phone_number = phone_number,
                           the_email = email,
                           the_address = address,
                           the_city = city,
                           the_state = state,
                           the_zip_code = zip_code,)

@app.route('/edit', methods=['POST'])
def edit() -> 'html':
    conn = sql.connect(host = 'localhost', user = 'root', password = 'Sounak@#$2004', database = 'participants')
    cursor = conn.cursor()
    global num_id, name, first_name, last_name, dob, gender, country_code, phone_number, email, address, city, state, zip_code
    num = request.form['num1']
    email = request.form['email']
    _SQL = "select * from log where id = %s and email = %s;"
    cursor.execute(_SQL, (num,
                          email,))
    data = cursor.fetchone()
    num = data[0]
    first_name = data[1]
    last_name = data[2]
    dob = data[3]
    gender = data[4]
    country_code = data[5]
    phone_number = data[6]
    email = data[7]
    address = data[8]
    city = data[9]
    state = data[10]
    zip_code = data[11]
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('edit.html',
                           the_id = num,
                           the_first_name = first_name,
                           the_last_name = last_name,
                           the_dob = dob,
                           the_gender = gender,
                           the_country_code = country_code,
                           the_phone_number = phone_number,
                           the_email = email,
                           the_address = address,
                           the_city = city,
                           the_state = state,
                           the_zip_code = zip_code,)


@app.route('/edited', methods=["POST"])
def edited() -> 'html':
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    gender = request.form['gender']
    country_code = request.form['country_code']
    phone_number = request.form['phone_number']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    result = {first_name, last_name, dob, gender, phone_number, email, address, city, state, zip_code}
    results = str(result)
    edit_request(request, results)
    return render_template('edited.html')

@app.route('/e3', methods=['POST'])
def e3() -> 'html':
    return render_template('e3.html')

@app.route('/delete', methods=['POST'])
def delete() -> 'html':
    import mysql.connector as sql
    conn = sql.connect(host = 'localhost',
                       user = 'root',
                       password = 'Sounak@#$2004',
                       database = 'participants')
    cursor = conn.cursor()
    num = request.form['num1']
    email = request.form['email']
    _SQL = "delete from log where id = %s and email = %s;"
    cursor.execute(_SQL, (num,
                          email,))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('delete.html')

if __name__=='__main__':
    app.run(debug=True)
