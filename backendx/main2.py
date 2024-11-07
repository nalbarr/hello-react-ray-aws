# NA
# - i.e., https://docs.ray.io/en/latest/serve/index.html

import requests
import starlette
from typing import Dict
from ray import serve
# NA
# - ray 2.4 does not support Deployment Handle
# from ray.serve.handle import DeploymentHandle

# NA
# - need explicity JSONResponse?
from starlette.responses import JSONResponse

# NA
# - add logger
import logging
serve_logger = logging.getLogger("ray.serve")
serve_logger.setLevel(logging.DEBUG)

# 1. Define the models in our composition graph and an ingress that calls them.
@serve.deployment
class Adder:
    def __init__(self, increment: int):
        self.increment = increment

    def add(self, inp: int):
        result = self.increment + inp
        serve_logger.info(f"*** Adder.add(): {result}")
        return result

@serve.deployment
class Combiner:
    def average(self, *inputs) -> float:
        result = sum(inputs) / len(inputs)
        serve_logger.info(f"*** Combiner.average(): {result}")        
        return result


@serve.deployment
class Ingress:
    '''
    def __init__(
        self,
        adder1: DeploymentHandle,
        adder2: DeploymentHandle,
        combiner: DeploymentHandle,
    ):
    '''
    def __init__(
        self,
        adder1,
        adder2,
        combiner,
    ):        
        self._adder1 = adder1
        self._adder2 = adder2
        self._combiner = combiner

    # NA
    # - Ray 2.4 does not like type hints?
    async def __call__(self, request: starlette.requests.Request) -> Dict[str, float]:
    # async def __call__(self, request) -> Dict[str, float]:     
        '''
        input_json = await request.json()
        serve_logger.info(f"*** input_json: {input_json}")
        final_result = await self._combiner.average.remote(
            self._adder1.add.remote(input_json["val"]),
            self._adder2.add.remote(input_json["val"]),
        )
        serve_logger.info(f"*** final_result: {final_result}")
        '''
        # NA
        # Q: why does below not work???
        input_json = {"val": 100.0}
        # input_json = await request.json()
        final_result = await self._combiner.average.remote(
            self._adder1.add.remote(input_json["val"]),
            self._adder2.add.remote(input_json["val"]),
        )
        # NA
        # - need explicit JSON response?
        # return {"result": final_result}
        
        # NA
        # Q: why does below not work???      
        json = JSONResponse({"val": 100.0})
        # json = JSONResponse({"result": final_result})
        return json

# 2. Build the application consisting of the models and ingress.
app = Ingress.bind(Adder.bind(increment=1), Adder.bind(increment=2), Combiner.bind())
serve.run(app)

# 3: Query the application and print the result.
# print(requests.post("http://localhost:8000/", json={"val": 100.0}).json())
# {"result": 101.5}