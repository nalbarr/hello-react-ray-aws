import httpx
import json

def test_request():
    params = {"val": 100.0}
    print(f"params: {params}")    
    print(f"type(params): {type(params)}")

    # NA
    # - NOTE: json has specific meaning as body with content type of JSON!
    result = httpx.get(url="http://localhost:8000", params=params)
    print(f"result: {result}")
    print(f"type(result): {type(result)}")

    result_json = result.json()
    print(f"result.json(): {result_json}")
    print(f"type(result_json): {type(result_json)}")
    

def main():
    test_request()

if __name__ == "__main__":
    main()