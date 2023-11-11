from flask import jsonify, request, Blueprint, render_template, current_app as app
from .models import JournalEntry
import json

journal = Blueprint('journal', __name__)
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
    return render_template('index.html')


@journal.route('/entries', methods=['GET'])
def list_entries():
    query = request.args.get('query', '').lower()
    filtered_entries = [entry for entry in entries if query in entry.title.lower()]
    return jsonify([entry.__dict__ for entry in filtered_entries])


@journal.route('/entry', methods=['POST'])
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


@journal.route('/entry/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    entry = next((e for e in entries if e.id == entry_id), None)
    if entry:
        return jsonify(entry.__dict__)
    return jsonify({"error": "Entry not found!"}), 404


@journal.route('/entry/<int:entry_id>', methods=['PUT'])
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


@journal.route('/entry/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    global entries
    entries = [e for e in entries if e.id != entry_id]
    return jsonify({"message": "Entry deleted!"})


@journal.route('/search', methods=['GET'])
def search_entries():
    query = request.args.get('query', '').lower()
    # Filter entries based on the query being in the title or the author's name
    filtered_entries = [entry for entry in entries if query in entry.title.lower() or query in entry.author.lower()]
    return render_template('search_page.html', entries=filtered_entries)


