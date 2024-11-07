import requests
import uvicorn
from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from ray import serve


@serve.deployment(route_prefix="/iris")
class BoostingModel:
    def __init__(self, model, label_list):
        self.model = model
        self.label_list = label_list

    async def __call__(self, request):
        payload = await request.json()["vector"]
        print(f"Received request with data {payload}")

        prediction = self.model.predict([payload])[0]
        human_name = self.label_list[prediction]
        return {"result": human_name}


def get_model():
    ### Returns iris trained model and dataset ###
    iris_dataset = load_iris()
    model = GradientBoostingClassifier()
    model.fit(iris_dataset["data"], iris_dataset["target"])

    return model, iris_dataset


def main():
    # Deploy model.
    # BoostingModel.deploy(model)

    model, iris_dataset = get_model()
    label_list = iris_dataset["target_names"].tolist()

    # handle = serve.run(BoostingModel.bind(model, iris_dataset))
    serve.run(BoostingModel.bind(model, label_list))
    # ray.get(handle.remote())

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()