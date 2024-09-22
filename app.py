from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def reverse_ip():
    # Get the client's IP address from the request headers
    client_ip = request.remote_addr

    # Reverse the IP address
    reversed_ip = '.'.join(client_ip.split('.')[::-1])

    # Return the reversed IP as a response
    return f"Your reversed IP is: {reversed_ip}"


if __name__ == '__main__':
    # Run the Flask app on port 5000 (default)
    app.run(host='0.0.0.0', port=5000)
