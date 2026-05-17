from fastapi import FastAPI

app = FastAPI(version="1.0.0", title="ghetto ticketmaster")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get(path="/event/{event_id}")
async def view_event(event_id: int):
    return {"event_id": event_id, "event_name": "give thanks", "performer": "illenium"}
