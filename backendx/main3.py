# NA
# - i.e., https://docs.ray.io/en/latest/serve/index.html

# import requests
# import starlette
from typing import Dict
from ray import serve
import logging

# NA
# - pivot main2.py to just use simple get

# NA
# - need explicity JSONResponse?
# from starlette.responses import JSONResponse

# NA
# - add logger
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
class Doubler:
    def double(self, x:float) -> float:
        result = 2 * x
        serve_logger.info(f"*** Doubler.double(): {result}")        
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
        # adder1,
        # adder2,
        # combiner,
        doubler,
    ):        
        # self._adder1 = adder1
        # self._adder2 = adder2
        # self._combiner = combiner
        self._doubler = doubler

    # NA
    # - Ray 2.4 does not like type hints?
    # async def __call__(self, request: starlette.requests.Request) -> Dict[str, float]:
    async def __call__(self, request) -> Dict[str, float]:     
        # val = 100.0
        val = request.query_params.get("val")
        '''
        result = await self._combiner.average.remote(
            self._adder1.add.remote(val),
            self._adder2.add.remote(val),
        )
        '''
        # NA
        # Q: why does below not work???    
        # result = await self._adder1.add.remote(val)
        # result = self._adder1.add.remote(val)
        result = await self._doubler.double.remote(val)
    
        # NA
        # - This always works
        json = {"result": val}
    
        # NA
        # Q: why does below not work???      
        # json = JSONResponse({"val": 100.0})
        # json = JSONResponse({"val": val})
        # json = JSONResponse({"result": result})
        # json = {"result": result}
     
        # NA.
        # Q: Why is below incorrect?
        # return await json
        return json


# NA
# - just reduce to Doubler for simple sky testing  
# app = Ingress.bind(Adder.bind(increment=1), Adder.bind(increment=2), Combiner.bind(), Doubler.bind())
app = Ingress.bind(Doubler.bind())

# NA
# - do not forget route_prefix and port !!!
# serve.run(app)
# serve.run(
#    app, name="pipeline", host="0.0.0.0", route_prefix="/", port=8000
# )
serve.run(
    app, name="pipeline", host="0.0.0.0", port=8000
)
