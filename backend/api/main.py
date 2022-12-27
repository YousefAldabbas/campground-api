from fastapi import FastAPI
from routes import routers
from config import Base,engine


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(routers)
