from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configuração de templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Simulação de dados
products = [
    {"id": 1, "name": "Vestido Floral", "price": 120.0, "description": "Vestido com estampa floral e tecido leve."},
    {"id": 2, "name": "Blusa Casual", "price": 80.0, "description": "Blusa de algodão com estilo casual."},
]

# Usuário fictício para autenticação
user_credentials = {"email": "luara@gmail.com", "password": "2010"}

# Variável para simular uma sessão
user_logged_in = False


# Página de login
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Processar o login
@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    global user_logged_in
    if email == user_credentials["email"] and password == user_credentials["password"]:
        user_logged_in = True
        return RedirectResponse("/home", status_code=303)
    return templates.TemplateResponse(
        "login.html",
        {"request": {}, "error": "Email ou senha incorretos!"},
    )


# Página inicial (listagem de produtos) - somente se logado
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    if not user_logged_in:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("index.html", {"request": request, "products": products})


# Formulário para adicionar/editar produto
@app.get("/form", response_class=HTMLResponse)
async def form(request: Request, id: int = None):
    if not user_logged_in:
        return RedirectResponse("/", status_code=303)
    product = next((p for p in products if p["id"] == id), None)
    return templates.TemplateResponse("form.html", {"request": request, "product": product})


# Adicionar produto
@app.post("/add")
async def add_product(name: str = Form(...), price: float = Form(...), description: str = Form(...)):
    if not user_logged_in:
        return RedirectResponse("/", status_code=303)
    new_id = max(p["id"] for p in products) + 1 if products else 1
    products.append({"id": new_id, "name": name, "price": price, "description": description})
    return RedirectResponse("/home", status_code=303)


# Editar produto
@app.post("/edit/{id}")
async def edit_product(id: int, name: str = Form(...), price: float = Form(...), description: str = Form(...)):
    if not user_logged_in:
        return RedirectResponse("/", status_code=303)
    product = next((p for p in products if p["id"] == id), None)
    if product:
        product["name"] = name
        product["price"] = price
        product["description"] = description
    return RedirectResponse("/home", status_code=303)


# Deletar produto
@app.get("/delete/{id}")
async def delete_product(id: int):
    global products
    if not user_logged_in:
        return RedirectResponse("/", status_code=303)
    products = [p for p in products if p["id"] != id]
    return RedirectResponse("/home", status_code=303)
