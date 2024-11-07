import requests

def test_hello_pipeline():
    params = {'x':2}
    response = requests.get(
        "http://localhost:8000/", params)
    print(response.text)

def main():
    test_hello_pipeline()

if __name__ == "__main__":
    main()