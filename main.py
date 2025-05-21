from fastapi import FastAPI, Request # 요청 
from fastapi.responses import HTMLResponse # 응답해주는 기능 중 HTML을 문서로 돌려줄 수 있는 기능들 
from fastapi.staticfiles import StaticFiles # css, js, image 등을 고정 폴더에 넣고 사용할 수 있게해주는 기능
from fastapi.templating import Jinja2Templates # template 폴더를 사용할 수 있게 해주는 기능 (Frontend)

# pip install fastapi
# pip install "uvicorn[standard]"
# pip install jinja2
# pip install fastapi "uvicorn[standard]" jinja2

app = FastAPI() # FastAPi 객체 생성

# 정적 파일 (JS, CSS 등) 제공 
# 폴더를 static이라고 만들고 JavaScript, CSS 파일은 다 static 파일에 넣어준다.
# 정적 파일들을 연결해준다는 뜻이다.
app.mount("/static", StaticFiles(directory="static"), name="static") 


# HTML 템플릿 디렉토리
# templates 라는 이름을 꼭 만들어서 html 파일을 만든다
# jinja2라는 템플릿을 디렉토리에연결해준다.
templates = Jinja2Templates(directory="templates")


# HTML 페이지 제공
# app.get 방식: url에 데이터를 실어서 넘겨주는 방식
# app.post 방식: url에 데이터를 숨겨서 넘겨주는 방식
@app.get("/", response_class=HTMLResponse) # 127.0.0.1:8000/ 라고 쓰면 도메인만 넣고 아무것도 안넣었을때 
async def get_page(request: Request): # 사용자가 서버쪽에 요청한 헤더정보가 들어간다. 
    return templates.TemplateResponse("index.html", {"request": request}) # 이쪽으로 들어와라

# 백엔드 API – JSON 데이터 제공
@app.get("/api/data")	# http://127.0.0.1:8000/api/data 를 호출했을때
async def get_data(): 
    return {"message": "FastAPI에서 보내는 데이터입니다"} # dictionary --> jason 형태로 변환해서 줌

