from pybricks.hubs import PrimeHub
from robot_config import HUB
from pybricks.tools import wait, multitask

# Music

async def star_wars_opening():
    #Define various measures
    x0 = ["D4/12", "D4/12", "D4/12"]
    x1 = ["G4/2", "D5/2"]
    x2 = ["C5/12", "B4/12", "A4/12", "G5/2",  "D5/4"]
    x3 = ["C5/12", "B4/12", "C5/12", "A4/2",  "D4/6", "D4/12"]
    x4 = ["E4/4.", "E4/8", "C5/8", "B4/8",  "A4/8", "G4/8"]
    x5 = ["G4/12", "A4/12", "B4/12", "A4/6", "E4/12", "F#4/4", "D4/6", "D4/12"]
    x6 = ["D5/4", "A4/2", "D4/6", "D4/12"]
    x7 = ["G4/12", "A4/12", "B4/12", "A4/6", "E4/12", "F#4/4", "D5/6", "D5/12"]
    x8 = ["G5/6", "F5/12", "Eb5/6", "D5/12", "C5/6", "Bb4/12", "A4/6", "G4/12"]
    x9 = ["D5/2."]
    x10 = ["G5/12", "F5/12", "Eb5/12", "Bb5/2", "A5/4", "G5/8", "R/8", "G4/12", "G4/12", "G4/12", "G4/4"]
    # Combine into the song
    song = x0 + x1 + x2 + x2 + x3 + x1 + x2 + x2 + x3 + x4 + x5 + x4 + x6 + x4 + x7 + x8 + x9 + x0 + x1 + x2 + x2 + x3 + x1 + x2 + x10
    # Play the song
    await HUB.speaker.play_notes(song)