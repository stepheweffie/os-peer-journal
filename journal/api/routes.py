from flask import jsonify, request, Blueprint, render_template, redirect, url_for, current_app as app
from models import JournalEntry
import json
import requests

api = Blueprint('journal', __name__)
current_id = 0  # This will help us assign unique IDs to entries


def load_entries():
    try:
        with open('entries.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_entries(all_entries):
    with open('entries.json', 'w') as f:
        json.dump(entries, f, default=lambda o: o.__dict__, indent=4)


@app.route('/')
def index():
    return redirect(url_for('api.search_entries'))


@api.route('/entries', methods=['GET'])
def list_entries():
    query = request.args.get('query', '').lower()
    filtered_entries = [entry for entry in entries if query in entry.title.lower()]
    return jsonify([entry.__dict__ for entry in filtered_entries])


@api.route('/entry', methods=['POST'])
def create_entry():
    global current_id
    entries = load_entries()
    title = request.json.get('title')
    author = request.json.get('author')
    thumbnail = request.json.get('thumbnail')
    abstract = request.json.get('abstract')
    content = request.json.get('content')

    if not title or not author or not thumbnail or not abstract or not content:
        return jsonify({"error": "All fields are required!"}), 400

    current_id += 1
    entry = JournalEntry(current_id, title, author, thumbnail, content)
    entries.append(entry)
    save_entries(entries)  # Save the updated list to the file
    return jsonify(entry.__dict__), 201


@api.route('/entry/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    entry = next((e for e in entries if e.id == entry_id), None)
    if entry:
        return jsonify(entry.__dict__)
    return jsonify({"error": "Entry not found!"}), 404


@api.route('/entry/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    entry = next((e for e in entries if e.id == entry_id), None)
    if not entry:
        return jsonify({"error": "Entry not found!"}), 404

    title = request.json.get('title')
    abstract = request.json.get('abstract')

    if title:
        entry.title = title
    if abstract:
        entry.content = abstract

    return jsonify(entry.__dict__)


@api.route('/entry/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    global entries
    entries = [e for e in entries if e.id != entry_id]
    return jsonify({"message": "Entry deleted!"})


@api.route('/search', methods=['GET'])
def search_entries():
    query = request.args.get('query', '').lower()
    # Filter entries based on the query being in the title or the author's name
    filtered_entries = [entry for entry in entries if query in entry.title.lower() or query in entry.author.lower()]
    return render_template('search_page.html', entries=filtered_entries)


@api.route('/generate_token', methods=['GET'])
def generate_token():
    # Make an HTTP POST request to the CherryPy web service to generate a token
    cherrypy_url = 'http://localhost:8080/generator'  # Replace with the actual URL of your CherryPy service
    response = requests.post(cherrypy_url)

    if response.status_code == 200:
        # Assuming the CherryPy service returns the token in the response
        token = response.text
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Failed to generate token"}), 500


