from fastapi import FastAPI as api
from v1.endpoints.index import router

app = api()
app.include_router(router, prefix='/v1')

@app.get('/')
def index():
    return {'status': 'OK!'}