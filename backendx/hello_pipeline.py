import requests
import starlette
from typing import Dict
import ray
from ray import serve
from ray.serve.handle import DeploymentHandle
import logging

@serve.deployment
class Step1:
    def add_two(self, x: int) -> int:
        result = x + 2
        return result


@serve.deployment
class Step2:
    def multiply_by_two(self, x: float) -> float:
        result = x * 2.0
        return result


@serve.deployment
class Pipeline:
    def __init__(
        self,
        step1: DeploymentHandle,
        step2: DeploymentHandle,
    ):        
        self._step1 = step1
        self._step2 = step2


    async def __call__(self, request:starlette.requests.Request) -> Dict[str, float]:     
        x = request.query_params.get("x")

        '''
        result = await self._step2.multiply_by_two(
            self._step1.add_two.remote(x)
        )
        '''
        x = await self._step1.add_two.remote(x)

        json = {"result": x}
        # json = {"result": result}
    
        return json


app = Pipeline.bind(Step1.bind(), Step2.bind())

handle: DeploymentHandle = serve.run(app)

response = handle.remote("2")
result = response.result()
print(f"result: {result}")
# assert response.result() == "Hello world!"

# serve.run(
#    app, name="pipeline", host="0.0.0.0", port=8000
# )

# NA
# - does NOT work
#     raise ValueError(
# ValueError: `detached=False` is no longer supported. In a future release, it will be removed altogether.
# - per Ray 2.9.3 documentation
# - i.e., https://docs.ray.io/en/latest/serve/api/doc/ray.serve.run.html
# 1. use serve.start over serve.run
# handle = serve.start(
#     app, name="pipeline", host="0.0.0.0", port=8000
# )

