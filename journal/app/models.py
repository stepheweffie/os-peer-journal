import datetime


class JournalEntry:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()