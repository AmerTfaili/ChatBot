from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import sys
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse  
from fastapi import Request, Response
from fastapi import FastAPI, HTTPException, File, UploadFile
app=FastAPI()
import groq


class TextRequest(BaseModel):
    query: str

@app.post("/groq-api/text")
async def groq_api_text(request: TextRequest):
    try:
        # Process the query text here
        response = {"message": f"Received query: {request.query}"}
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))