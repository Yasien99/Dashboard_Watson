from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
  # Get data from request body
  data = request.get_json()

  # **Placeholder for sending data to external DB**
  # Replace with your specific DB interaction logic
  print(f"Received data: {data}")

  # Return success message
  return jsonify({'message': 'Data received successfully!'}), 201

if __name__ == '__main__':
  app.run(debug=True)
