from fastapi import FastAPI
from api.health import router as health_router
from api.model import router as model_router
from api.task import router as task_router
from api.image import router as image_router
from api.run import router as run_router
from api.status import router as status_router
from api.result import router as result_router
from api.cancel import router as cancel_router

app = FastAPI(
    title="Wind Blade AI Service",
    version="1.0.0",
    description="Wind Blade Defect Detection API",
)

@app.get("/")
def root():
    return {"message": "Wind Blade AI Service is running."}
app.include_router(health_router)
app.include_router(model_router)
app.include_router(task_router)
app.include_router(image_router)
app.include_router(run_router)
app.include_router(status_router)
app.include_router(result_router)
app.include_router(cancel_router)