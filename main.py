from fastapi import FastAPI

app = FastAPI(title='Training app')




@app.get("/")
async def get_hello():
    return {"message": "Hello World"}