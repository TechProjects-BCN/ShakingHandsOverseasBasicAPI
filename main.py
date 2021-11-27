from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

status = {}
F = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")   
def home():
    return {"Shaking Hands Overseas" : "API"}

@app.post("/servo")
def servo(Info: dict):
    status["s1"] = Info["s1"]
    status["s2"] = Info["s2"]
    status["s3"] = Info["s3"]
    status["s4"] = Info["s4"]
    status["s5"] = Info["s5"]
    
    return {'s1': status["s1"], 
            's2': status["s2"], 
            's3': status["s3"], 
            's4': status["s4"], 
            's5': status["s5"]
            }

@app.post('/custom')
def custom(custom: dict):
    F[0] = custom["F1"]
    F[1] = custom["F2"]
    F[2] = custom["F3"]
    F[3] = custom["F4"]
    F[4] = custom["F5"]



@app.get("/reciever")
def reciever():
    return {'s1': status[F[0]], 
            's2': status[F[1]], 
            's3': status[F[2]], 
            's4': status[F[3]], 
            's5': status[F[4]]
            }
