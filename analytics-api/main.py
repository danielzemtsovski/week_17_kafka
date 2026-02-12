from fastapi import FastAPI

app = FastAPI()

@app.get("/analytics/top-customers")
def a():
    return

@app.get("/analytics/customers-without-orders")
def a():
    return

@app.get("/analytics/zero-credit-active-customers")
def a():
    return