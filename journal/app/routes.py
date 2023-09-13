from flask import jsonify, request, Blueprint
from models import JournalEntry


journal = Blueprint('journal', __name__)
entries = []  # This will act as our in-memory database
current_id = 0  # This will help us assign unique IDs to entries


@journal.route('/entries', methods=['GET'])
def list_entries():
    return jsonify([entry.__dict__ for entry in entries])


@journal.route('/entry', methods=['POST'])
def create_entry():
    global current_id
    title = request.json.get('title')
    content = request.json.get('content')

    if not title or not content:
        return jsonify({"error": "Title and content are required!"}), 400

    current_id += 1
    entry = JournalEntry(current_id, title, content)
    entries.append(entry)

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
    content = request.json.get('content')

    if title:
        entry.title = title
    if content:
        entry.content = content

    return jsonify(entry.__dict__)


@journal.route('/entry/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    global entries
    entries = [e for e in entries if e.id != entry_id]
    return jsonify({"message": "Entry deleted!"})
