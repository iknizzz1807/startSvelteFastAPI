from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from contextlib import asynccontextmanager
from fastapi import HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "sqlite:///./test.db"


database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await database.connect()
        yield
    finally:
        await database.disconnect()


app = FastAPI(lifespan=lifespan)

# Tell the CORS to shut up
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#


class ItemCreate(BaseModel):
    name: str
    description: str


@app.post("/items")
async def create_item(item: ItemCreate):
    query = Item.__table__.insert().values(**item.model_dump())
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.get("/items")
async def read_item():
    query = Item.__table__.select()
    result = await database.fetch_all(query)
    return result
