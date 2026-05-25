from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from controller import rota  

app = FastAPI()
app.include_router(rota)    



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
            
       
    
    
if __name__ == "__main__":  
    import uvicorn  
  
    uvicorn.run(app, host="localhost", port=7000)