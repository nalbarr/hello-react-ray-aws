from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    print("hello")
    return {"message": "hello"}

def hello():
    uvicorn.run("hello:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    hello()
