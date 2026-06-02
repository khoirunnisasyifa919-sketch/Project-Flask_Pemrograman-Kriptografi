from flask import Flask, render_template, request

application = Flask(__name__)

def encrypt(teks):
    hasil = ""
    for huruf in teks:
        hasil += chr(ord(huruf) + 3)
    return hasil

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama_depan = request.form['nama_depan']
        nama_belakang = request.form['nama_belakang']

        nama = nama_depan + " " + nama_belakang
        nama_encrypt = encrypt(nama)

        return render_template(
            'hasil.html',
            nama=nama,
            nama_encrypt=nama_encrypt
        )

    return render_template('index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
