from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Attendee(BaseModel):
    name: str
    phone: str
    email: str
    vegetarian: bool
    drinks_alcohol: bool

attendees = []

@app.post("/register")
def register_attendee(attendee: Attendee):
    attendees.append(attendee)
    return {"message": "Anmeldung erfolgreich"}

@app.get("/attendees")
def get_attendees():
    return attendees
