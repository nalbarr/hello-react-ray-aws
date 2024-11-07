from ray import serve
from ray.serve.handle import DeploymentHandle

@serve.deployment
class Adder:
    def add(self, val: int) -> int:
        return val + 1

@serve.deployment
class Caller:
    def __init__(self, handle: DeploymentHandle):
        self._adder_handle = handle

async def __call__(self, start: int) -> int:
    return await self._adder_handle.add.remote(
        # Pass the response directly to another handle call without awaiting.
        self._adder_handle.add.remote(start)
    )

app = Caller.bind(Adder.bind())
handle: DeploymentHandle = serve.run(app)

response = handle.remote(0)
print(response.result())
