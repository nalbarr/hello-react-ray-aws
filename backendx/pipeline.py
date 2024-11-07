# import ray
from ray import serve
# from ray.serve.handle import DeploymentHandle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import uvicorn
import logging

serve_logger = logging.getLogger("ray.serve")
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


@app.get("/")
def health_check():
    return "health check."

# @serve.ingress(app)
@serve.deployment(route_prefix="/pipeline")
class Pipeline:
    def __init__(self, adder, multipler):
        self._adder = adder
        self._multiplier = multipler

    '''
    @app.get("/predict")
    def method(self, x: int):
        def double(x: int):
            return 2 * x

        def getJson(x: int):
            y = double(x)
            json = JSONResponse({'y': y})
            return json

        return getJson(x)        
    '''

    async def __call__(self, http_request):
        x = http_request.query_params.get("x")
        serve_logger.info(f"pipeline called with {x}")

        if not x:
            return "UP"
        # add two
        # x2_ref = await self._adder.add_by_two.remote(x)
        # x2 = ray.get(x2_ref)
        # multiply by two
        # x3_ref = await self._multiplier.multiply_by_two.remote(x2)
        # x3 = ray.get(x3_ref)

        x = int(x)
        print(f"type(x): {type(x)}")
        x3 = await self._adder.add_by_two.remote(2)

        return x3
 

@serve.deployment()
class Adder:
    def add_by_two(self, x):
        return x + 2

@serve.deployment()
class Multiplier:   
    def multiply_by_two(self, x):
        return x * 2


def main():
    
    pipeline = Pipeline.bind(Adder.bind(), Multiplier.bind())
    handle = serve.run(pipeline)
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()