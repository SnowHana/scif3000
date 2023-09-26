import requests

# The URL of the CSV file
url = "https://opennem.org.au/energy/nem/?range=7d&interval=30m&format=csv"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content of the response to a local file
    with open("energy_data.csv", "wb") as file:
        file.write(response.content)
else:
    print("Failed to retrieve the CSV file.")
