import datetime


class JournalEntry:
    def __init__(self, id, title, author, thumbnail, abstract, content):
        self.id = id
        self.title = title
        self.author = author
        self.thumbnail = thumbnail
        self.abstract = abstract
        self.content = content
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()