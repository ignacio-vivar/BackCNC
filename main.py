from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from api.youtube_service import get_videos_from_playlist

app = FastAPI()

origins = [
    "https://cncwebpage.netlify.app/",
    "https://main--cncwebpage.netlify.app/"
 # Tu dominio de producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,  # Permitir credenciales (cookies, autenticación, etc.)
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/")
def default():
    return {
        "mensaje" : "actualizado 8/9"
    }
# Trabajos Prácticos
@app.get("/tps")
def tps_list():
    return{ 
        "tps": [
            {"id" : 0, "file": "TP0.pdf", "name" : "Trabajo Práctico N°0"}, 
            {"id" : 1, "file": "TP1.pdf", "name" : "Trabajo Práctico N°1"}, 
            {"id" : 2, "file" : "TP2.pdf", "name" : "Trabajo Práctico N°2"},
            {"id" : 3, "file" : "TP3.pdf", "name" : "Trabajo Práctico N°3"},
            {"id" : 4, "file" : "TP4.pdf", "name" : "Trabajo Práctico N°4"},
            {"id" : 5, "file" : "TP5.pdf", "name" : "Trabajo Práctico N°5"},
                ]
        }

@app.get("/files/{filename}")
def files(filename: str):
    headers = {
        "Content-Disposition": f'inline; filename="{filename}"'
    }
    return FileResponse(
        path=f"uploads/tps/{filename}",
        headers=headers)

@app.get("/dfiles/{filename}")
def files(filename: str):
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"'
    }
    return FileResponse(
        path=f"uploads/tps/{filename}",
        headers=headers)

# Guías Manuales

@app.get("/manuales")
def manuales():
    return {
        "manuales" : [
            {"id": 0, "file":"manualFull.pdf", "title":"Manual CNC Completo", "thumbnail" : "full.jpg", "alt":"Imagen Libro"},
            {"id": 1, "file":"manualResumido.pdf", "title":"Manual CNC Resumido", "thumbnail" : "resum.jpg", "alt":"Imagen Libro Resumen"},
        ]
    }

@app.get("/dmanuals/{filename}")
def files(filename: str):
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"'
    }
    return FileResponse(
        path=f"uploads/manuales/{filename}",
        headers=headers)


@app.get("/tmanuals/{filename}")
def files(filename: str):
    headers = {
        "Content-Disposition": f'inline; filename="{filename}"'
    }
    return FileResponse(
        path=f"uploads/manuales/thumbnails/{filename}",
        headers=headers)


# Guías SSCNC

@app.get("/sscnc")
def manuales():
    return {
        "sscnc": [
            {"id": 0, "file":"Guia1.pdf","title": "Guia 1" , "desc":"Básicos del Simulador"},
            {"id": 1, "file":"Guia2.pdf","title": "Guia 2" , "desc":"Referencias del Simulador (1/2)"},
            {"id": 2, "file":"Guia3.pdf","title": "Guia 3" , "desc":"Referencias del Simulador (2/2)"},
            {"id": 3, "file":"Guia4.pdf","title": "Guia 4" , "desc":"Programas en el Simulador"},
        ]
    }

@app.get("/dsscnc/{filename}")
def files(filename: str):
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"'
    }
    return FileResponse(
        path=f"uploads/guias/{filename}",
        headers=headers)


# Obtención de videos

@app.get("/playlist/")
async def get_playlist_videos(playlist_url: str):
    try:
        # Llama a la función del módulo youtube_service para obtener los videos
        videos = get_videos_from_playlist(playlist_url)
        return {"videos": videos}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error inesperado en el servidor")
    

# Lista de programas

@app.get("/programs")
def programs():
    return{
        "programs":[
            {"id":0, "name": "Obsidian", "url": "https://obsidian.md/download", "file":"obsidian.png"},
            {"id":1, "name": "LightShot", "url": "https://app.prntscr.com/es/download.html" , "file":"lightshot.webp"},
            {"id":2, "name": "SumatraPDF", "url": "https://www.sumatrapdfreader.org/download-free-pdf-viewer" , "file":"sumatra.ico"},
        ]
    }

@app.get("/programs/{filename}")
def files(filename: str):
    headers = {
        "Content-Disposition": f'inline; filename="{filename}"'
    }
    return FileResponse(
        path=f"uploads/icons/{filename}",
        headers=headers)