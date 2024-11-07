from fastapi import fastapi
from tortoise.contrib.fastapi import register_tortoise

async def configure_db(app: FastAPI):
    register_tortoise{
        app=app,
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
        }
    }