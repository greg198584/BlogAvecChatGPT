from app import app, db
from flask_migrate import Migrate

# Créez une instance de Migrate pour gérer les migrations
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
