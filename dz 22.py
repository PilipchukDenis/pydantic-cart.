# 1.Создать ручку для получения html и отрисовки его в браузере

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def get_html():
#     return "<html><body><h1>Hello, World!</h1></body></html>"
#
# if __name__ == '__main__':
#     app.run(debug=True)

# ______________________

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
#
#
# class CartItem(BaseModel):
#     name: str
#     price: float
#     quantity: int
#
# cart_items = [
#     CartItem(name="Товар 1", price=100.0, quantity=2),
#     CartItem(name="Товар 2", price=50.0, quantity=1),
# ]
#
# app = FastAPI()
#
#
# @app.get("/cart", response_model=List[CartItem])
# def get_cart_items():
#     return cart_items



# 2. создать ручку для получения списка пайдентик моделей сарт.

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
#
#
# class Cart(BaseModel):
#     item_id: int
# quantity: int
#
#
# app = FastAPI()
#
#
# carts = [
# Cart(item_id=1, quantity=2),
# Cart(item_id=2, quantity=1),
# Cart(item_id=3, quantity=3)
# ]
#
#
# @app.get("/carts", response_model=List[Cart])
# async def get_carts():
#     return carts
# if __name__ == "__main__":
#     import uvicorn
# uvicorn.run(app, host="127.0.0.1", port=8000)
