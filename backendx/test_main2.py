import requests
import json

def test_request():
    json = {"val": 100.0}
    print(f"json: {json}")    
    print(f"type(json): {type(json)}")

    # NA
    # - NOTE: json has specific meaning as body with content type of JSON!
    result = requests.post("http://localhost:8000", json)
    print(f"result: {result}")
    print(f"type(result): {type(result)}")

    result_json = result.json()
    print(f"result.json(): {result_json}")
    print(f"type(result_json): {type(result_json)}")
    

def main():
    test_request()

if __name__ == "__main__":
    main()