from fastapi import FastAPI
import uvicorn  
from core.settings import PORT, DEBUG, set_routers, use_session

app = FastAPI()

set_routers(app=app)
use_session(app=app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=DEBUG)