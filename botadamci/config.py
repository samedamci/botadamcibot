from os import getenv, getcwd
import json

TOKEN = getenv("TOKEN")

with open(f"{getcwd()}/data/federation.json", "r") as f:
    FEDERATION = json.loads(f.read())
