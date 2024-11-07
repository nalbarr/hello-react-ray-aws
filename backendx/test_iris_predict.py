import requests

def test_iris_predict():
    sample_request_input = {"vector": [1.2, 1.0, 1.1, 0.9]}
    response = requests.get(
        "http://localhost:8000/iris", json=sample_request_input)
    print(response.text)

def main():
    test_iris_predict()

if __name__ == "__main__":
    main()