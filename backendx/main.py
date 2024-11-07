import ray
from ray import serve
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import uvicorn


app = FastAPI()
# NA
# - allow any origins for now.
# origins = [
#     "http://localhost",  
#     "http://localhost:3000",
# ]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NA
# - not needed
# ray.init(address="auto", namespace="backendx")

# NA. Expose port
# - not needed; use uvicorn
# serve.start(detached=True)
# serve.start(detached=True, http_options={"host": "0.0.0.0"})

@app.get("/")
def health_check():
    return "health check."

'''
@app.get("/simples")
async def simples():
    return {"x": 1}

@app.get("/predict")
async def predict():
    return {"y": 2}    
'''

'''
@serve.deployment(route_prefix="/api1")
@serve.ingress(app)
class Model1:
    @app.get("/predict")
    def method(self):
        return "Predict 1!"

@serve.deployment(route_prefix="/api2")
@serve.ingress(app)
class Model2:
    @app.get("/predict")
    def method(self, x: int):
        def double(x: int):
            return 2 * x

        return "Predict 2! y: " + str(double(x))
'''

@serve.deployment(route_prefix="/api3")
@serve.ingress(app)
class Model3:
    @app.get("/predict")
    def method(self, x: int):
        def double(x: int):
            return 2 * x

        def getJson(x: int):
            # NA.
            # NOTE:
            # - MP below are hard wired to construct JSON but you need to formally JSON encode
            # return '{"y": 4}'
            # return '{"y:"' + str(double(x)) + "}"
            # return '{"y": {0}}'.format(y)
            # return JSON.stringify(json)
            y = double(x)
            json = JSONResponse({'y': y})
            return json

        return getJson(x)        


def main():
    
    # Model1.deploy()
    # Model2.deploy()
    # NA. Just use model 3 for testing passed param1
        
    # NA
    # - deprecated
    # Model3.deploy()
    handle = serve.run(Model3.bind())

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()