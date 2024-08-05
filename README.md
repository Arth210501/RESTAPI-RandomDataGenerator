# Explanation:

Flask Setup: Import and set up Flask to create the REST API.
Faker Initialization: Create a Faker instance to generate realistic data.
Data Generation Function: generate_random_data function generates a list of dictionaries with sequential userId values and random data for each specified column.
API Endpoint: Define a route /api/data to handle GET requests. This route calls the data generation function and returns the JSON data.
Run the Application: Run the Flask application in debug mode.
