import requests

# The API endpoint
url = "http://127.0.0.1:5000/api/v1/books"

# Delete first 5 books (IDs 0-4)
for i in range(0, 5):
    response = requests.delete(f"{url}/{i}")
    print(f"Deleted book id: {i} - Status: {response.status_code}")

# Delete last 5 books (IDs 40-44 that we previously added)
for i in range(40, 45):
    response = requests.delete(f"{url}/{i}")
    print(f"Deleted book id: {i} - Status: {response.status_code}")


