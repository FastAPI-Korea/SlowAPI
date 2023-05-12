import uvicorn
from fastapi import FastAPI, Path

app: FastAPI = FastAPI()


@app.get("/hello/{name}")
def greeting(name: str = Path(default=..., description="User name to greet")) -> dict[str, str]:
    return {"detail": f"Hello, {name}"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)
