from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 모든 도메인에서의 요청 허용 (개발용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 데이터 모델 정의
class TestRequest(BaseModel):
    message: str

# 테스트 엔드포인트
@app.post("/test")
async def test_endpoint(request: TestRequest):
    return {"received_message": request.message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
