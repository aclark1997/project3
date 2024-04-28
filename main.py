from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from fastapi.responses import HTMLResponse

from models import AutoModels

engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@db:5432/dvdrental", echo=True
)


auto_models = None


async def lifespan(app):
    print("startup")
    global auto_models
    auto_models = await AutoModels.create(engine)
    yield
    print("shutdown")


app = FastAPI(lifespan=lifespan)


@app.get("/api/v1/hello")
async def root():
    return {"message": "Hello World"}


@app.get("/film/{id}", response_class=HTMLResponse)
async def film(id: int):
    with open("ui/dist/film.html") as file:
        return file.read()

@app.delete("/api/v1/film/{id}")
async def api_v1_film_delete(id: int):
    Film = await auto_models.get("film")

    async with AsyncSession(engine) as session:
        # TODO: fetch the film from the database here
        film = await session.execute(select(Film).where(Film.film_id == id))
        if film:
            await session.delete(film.scalar())
            await session.commit()
            return {"ok": True}
        else:
            return {"ok": False, "reason": "not found"}

@app.get("/api/v1/film/{id}")
async def api_film(id: int):
    Film = await auto_models.get("film")
    result = {}
    
    async with AsyncSession(engine) as session:
        film = await session.execute(select(Film).where(Film.film_id == id))
        scalar = film.scalar()
        result = scalar #{
            #"title": scalar.title,
            #"description": scalar.description,
            #"id": scalar.film_id
        #}
    return result

@app.get("/api/v1/films")
async def films():
    Film = await auto_models.get("film")

    results = []

    async with AsyncSession(engine) as session:
        films = await session.execute(select(Film))
        for film in films.scalars().all():
            results.append(
                {
                    "title": film.title,
                    "description": film.description,
                    "id": film.film_id,
                })
    return results


app.mount("/", StaticFiles(directory="ui/dist", html=True), name="ui")
