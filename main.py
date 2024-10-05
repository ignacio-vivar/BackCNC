from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from api.youtube_service import get_videos_from_playlist

app = FastAPI()

origins = [
    # "http://localhost:5173",
    # "http://192.168.100.5:5173",
    "https://cncwebpage.netlify.app",
    "https://main--cncwebpage.netlify.app"
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
        "mensaje" : "actualizado 8/9 22:15"
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
            {"id": 2, "file":"TeoriaTP1.pdf", "title":"Teoria Trabajo Práctico N°1", "thumbnail" : "teoriaTPS.jpg", "alt":"Imagen Teoría TPS"},
            {"id": 3, "file":"TeoriaTP2.pdf", "title":"Teoría Trabajo Práctico N°2", "thumbnail" : "teoriaTPS.jpg", "alt":"Imagen Teoría TPS"},
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

# @app.get("/playlist/")
# async def get_playlist_videos(playlist_url: str):
#     try:
#         # Llama a la función del módulo youtube_service para obtener los videos
#         videos = get_videos_from_playlist(playlist_url)
#         return {"videos": videos}
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Error inesperado en el servidor")

@app.get("/playlist/")
def get_videos_static():
    return{
        
    "videos": [
        {
            "title": "01 Introducci\u00f3n",
            "video_url": "https://youtube.com/watch?v=bP4OYWBRlOQ",
            "thumbnail_url": "https://i.ytimg.com/vi/bP4OYWBRlOQ/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGkgEyh_MA8=&rs=AOn4CLChbPUg0wf9oO3jXjvLANzKKP0qkQ"
        },
        {
            "title": "02 ProgramaInicio",
            "video_url": "https://youtube.com/watch?v=r2jd293ELPs",
            "thumbnail_url": "https://i.ytimg.com/vi/r2jd293ELPs/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGkgEyh_MA8=&rs=AOn4CLA1aDUlmMQdFI6dLfSS_kbLHplVOA"
        },
        {
            "title": "03 ReferenciarBasico",
            "video_url": "https://youtube.com/watch?v=r3Y9a6egLn0",
            "thumbnail_url": "https://i.ytimg.com/vi/r3Y9a6egLn0/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGBMgTSh_MA8=&rs=AOn4CLAQpMbzDKKbpXOAxwt1c7VMmN2MLw"
        },
        {
            "title": "04 SeleccionPieza",
            "video_url": "https://youtube.com/watch?v=zwZHcxDSjFY",
            "thumbnail_url": "https://i.ytimg.com/vi/zwZHcxDSjFY/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTSh_MA8=&rs=AOn4CLDBpoH_9zVBe69qj0OzVcsMEFzFqA"
        },
        {
            "title": "05 SelectInsertos",
            "video_url": "https://youtube.com/watch?v=gaEGPBMQujs",
            "thumbnail_url": "https://i.ytimg.com/vi/gaEGPBMQujs/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTih_MA8=&rs=AOn4CLDw3R6CrlfDsmyVfMmJ6Yiw15gsqw"
        },
        {
            "title": "06 PosicionamientoRapido",
            "video_url": "https://youtube.com/watch?v=Vp2E_KWUK5o",
            "thumbnail_url": "https://i.ytimg.com/vi/Vp2E_KWUK5o/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTih_MA8=&rs=AOn4CLDGaUNwM2AZ9Y0-UoM1Y_4vPFqrAA"
        },
        {
            "title": "07 MeasureWorkPiece",
            "video_url": "https://youtube.com/watch?v=muAbsBkwZ0Q",
            "thumbnail_url": "https://i.ytimg.com/vi/muAbsBkwZ0Q/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTih_MA8=&rs=AOn4CLCCk1m1zIukZPmqcpmeDtDC1qQsuQ"
        },
        {
            "title": "08 OffsetParam",
            "video_url": "https://youtube.com/watch?v=EASqCwGE9LY",
            "thumbnail_url": "https://i.ytimg.com/vi/EASqCwGE9LY/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTSh_MA8=&rs=AOn4CLAIkB2mH9TC2a_FW8yhRHcjURjNEg"
        },
        {
            "title": "09 ToolMeasure",
            "video_url": "https://youtube.com/watch?v=ExCiiToHbyc",
            "thumbnail_url": "https://i.ytimg.com/vi/ExCiiToHbyc/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTih_MA8=&rs=AOn4CLBBnYKTgv0M5bcUIOhR-ME2_E5alg"
        },
        {
            "title": "10 Programas",
            "video_url": "https://youtube.com/watch?v=VUMJssSJ8VI",
            "thumbnail_url": "https://i.ytimg.com/vi/VUMJssSJ8VI/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTih_MA8=&rs=AOn4CLCsTofTzP-hnxde3ipHGNg6gkHqRQ"
        },
        {
            "title": "11 DondeEstaMiCodigo",
            "video_url": "https://youtube.com/watch?v=ni0-aw4kM1U",
            "thumbnail_url": "https://i.ytimg.com/vi/ni0-aw4kM1U/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGGkgEyh_MA8=&rs=AOn4CLA3ivvGjDDRTC6uIUiQELaAZ77T9A"
        },
        {
            "title": "12 EjecutarPrograma",
            "video_url": "https://youtube.com/watch?v=OokvaGIzrLI",
            "thumbnail_url": "https://i.ytimg.com/vi/OokvaGIzrLI/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTSh_MA8=&rs=AOn4CLBDFA7Z3LiKyVDwuh41n8V99akOaw"
        },
        {
            "title": "13 Colisiones",
            "video_url": "https://youtube.com/watch?v=C637qWpy1AI",
            "thumbnail_url": "https://i.ytimg.com/vi/C637qWpy1AI/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTSh_MA8=&rs=AOn4CLBzZk3u_KpDHXjBf8d4k3cfSsePiw"
        },
        {
            "title": "14 Generalidades",
            "video_url": "https://youtube.com/watch?v=d3c63NDF13g",
            "thumbnail_url": "https://i.ytimg.com/vi/d3c63NDF13g/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACzgWKAgwIABABGBMgTSh_MA8=&rs=AOn4CLCd3LHcq5h02l69yuEY8FXFlDcjFQ"
        }
    ]
}
    

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