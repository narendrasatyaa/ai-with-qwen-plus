# app.py
import streamlit as st
import dashscope
from dashscope import Generation
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Konfigurasi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Untuk development, batasi di production
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Set API key Anda
DASHSCOPE_API_KEY = 'sk-95a168a9cefd4f2fb5a3c1b7847929fc'
dashscope.api_key = DASHSCOPE_API_KEY
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'

@app.post("/generate")
async def generate_questions(request: Request):
    try:
        data = await request.json()
        topic = data.get('topic')
        language = data.get('language', 'Bahasa Indonesia')
        count = data.get('count', 15)
        
        if not topic:
            raise HTTPException(status_code=400, detail="Topik harus diisi")
        
        prompt = f"""
        Buatkan {count} pertanyaan psikologi dalam bahasa {language} tentang topik {topic}.
        Pertanyaan harus menggunakan skala Likert 1-4 dengan pilihan:
        1: Sangat Tidak Setuju
        2: Tidak Setuju
        3: Setuju
        4: Sangat Setuju
        
        Format output harus berupa array JSON dengan setiap elemen adalah string pertanyaan.
        Contoh: ["Pertanyaan 1", "Pertanyaan 2", ...]
        """
        
        response = Generation.call(
            model='qwen-plus',
            prompt=prompt,
            result_format='text'
        )
        
        # Parsing response untuk ekstrak pertanyaan
        # HATI-HATI: eval() tidak aman untuk production
        questions = eval(response.output.text)  
        
        return {"questions": questions}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Streamlit UI
def streamlit_app():
    st.title("🤖 Qwen-Plus AI Gateway")
    st.write("Endpoint ini menangani pembuatan pertanyaan untuk Kenal Batin")

if __name__ == "__main__":
    import threading
    # Jalankan FastAPI di thread terpisah
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=8000)).start()
    # Jalankan Streamlit
    streamlit_app()
