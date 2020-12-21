import requests as req


def main():
    base_domain = "http://10.10.88.151:8000/api/"  # Domain root for API requests

    for i in range(1, 101):
        if (i % 2 != 0):
            api_response = req.get(base_domain + str(i))
            print(api_response.text)


if __name__ == "__main__":
    main()
