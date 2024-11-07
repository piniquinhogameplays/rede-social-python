from fastapi import FastAPI

def create_app():

    app = FastAPI()

    #Inicialização db/tortoise
    configure_db(app)

    return app
app = create_app()


@app.get('/')
async def home():
    return('status': 'ok')