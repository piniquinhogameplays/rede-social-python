from fastapi import fastapi
from tortoise.contrib.fastapi import register_tortoise

def configure_db(app: FastAPI):
    register_tortoise{
        app=app,
        db_url="sqlite://db.sqlite3",
        modules={"models": ["models"]},
        # db_url="postgres://postgres:qwert123@localhost:5432/events"
        config={
            "Connections": {
                # 'default': "postgres://postgres:qwerty123@localhost:5432/events"
                'default': 'sqllite://db.slqlite.3'
            },
            "apps": {
                'models': {
                    'model': [],
                    'default_connection': 'default',
                }
            }
        },
        generate_schema=True,
        add_exception_handlers=True,,
    }

# Executa comando no CMD task dev     
# para sair aperte CTRL + C 