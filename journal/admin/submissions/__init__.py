from app import create_app, db
'''
python __init__.py
'''

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creating tables if they don't exist
    app.run()