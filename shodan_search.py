import shodan
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Query the shodan API")
parser.add_argument("query", type=str, help="Search query")
args = parser.parse_args()

# Assign API key into a variable
API_KEY = "YOUR_API_KEY_HERE"

# Initialize the Shodan client
api = shodan.Shodan(API_KEY)

# Function to generate URLs with both http and https
def generate_urls(ip, port):
    return [f'http://{ip}:{port}', f'https://{ip}:{port}']

# Perform the search
try:
    results = api.search(args.query)
    print(f'Results found: {results["total"]}\n')

    # Display results
    for result in results['matches']:
        ip = result['ip_str']
        port = result['port']
        if 'hostnames' in result:
            hostnames = ", ".join(result['hostnames'])
        else:
            hostnames = "No hostnames available"
        urls = generate_urls(ip, port)
        print(f'IP: {ip}')
        print(f'Port: {port}')
        print(f'Hostnames (URL): {hostnames}')
        print(f'Links: {", ".join(urls)}\n')

except shodan.APIError as e:
    print(f'Error: {e}')