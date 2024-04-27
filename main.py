from fastapi import FastAPI
import uvicorn

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using a decorator
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

