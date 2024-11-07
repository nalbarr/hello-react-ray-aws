import requests

def test_pipeline():
    params = {'x':2}
    response = requests.get(
        "http://localhost:8000/pipeline", params)
    print(response.text)

def main():
    test_pipeline()

if __name__ == "__main__":
    main()