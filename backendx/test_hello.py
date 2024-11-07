import httpx
import json

def test_request():
    result = httpx.get(url="http://localhost:8000")
    print(f"result: {result}")


def main():
    test_request()


if __name__ == "__main__":
    main()
