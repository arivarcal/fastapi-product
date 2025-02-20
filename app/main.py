import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.db import create_db_and_tables

from app.tasks import routers as Task
from app.products import routers as Product
from app.products_category import routers as ProductCategory
from app.products_brand import routers as ProductBrand
from app.customers import routers as Customer
app = FastAPI()

version = "v1"

description = """
API de un Sistema de tareas y productos, usando FastApi con Python.

Funciones;
- Crear, Leer, Actualizar y eliminar Tareas
"""

version_prefix = f"/api/{version}"


app = FastAPI(
    lifespan=create_db_and_tables,
    title="AppTransactionFastAPI Ariel",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Ariel Azarias Vargas Calvimontes",
        "url": "https://github.com/arivarcal",
        "email": "arivarcal@gmail.com",
    },
    openapi_tags=[
        {
            "name": "Tasks",
            "description": "Lista de Tareas",
        },
        {
            "name": "Products",
            "description": "Lista de Products",
        },
        {
            "name": "Customers",
            "description": "Lista de Customers",
        },
    ],
)
app.include_router(Task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(Product.router, prefix="/products", tags=["Products"])
app.include_router(ProductCategory.router, prefix="/products_category", tags=["Products Category"])
app.include_router(ProductBrand.router, prefix="/products_brand", tags=["Products Brand"])
app.include_router(Customer.router, prefix="/customers", tags=["Customers"])


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Bienvenido</title>
        </head>
        <body>
            <h1>API con FastAPI!</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)