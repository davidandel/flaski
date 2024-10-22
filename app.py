from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)

client = MongoClient(host='test_mongodb', port=27017, username='root', password='pass', authSource="admin")
db = client.mylibrarydb
books_collection = db.books

# Nastavíme adresář pro ukládání obrázků
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Vytvoření adresáře, pokud neexistuje
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    books = books_collection.find()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    description = request.form.get('description')
    image = request.files.get('image')

    if title and author and image and description:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)
        books_collection.insert_one({
            'title': title,
            'author': author,
            'description': description,
            'image': image.filename
        })

    return redirect(url_for('index'))

@app.route('/delete_book/<book_id>', methods=['GET'])
def delete_book(book_id):
    books_collection.delete_one({'_id': ObjectId(book_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
