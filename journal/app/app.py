from __init__ import create_app
'''
Published submissions to publishedpapers.db go into the api reference.
Journal entries are published to the front page of the journal, styled with links, and part of
the readable presentation content.
'''

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        pass
        # db.create_all()  # Creating tables if they don't exist
    app.run()

