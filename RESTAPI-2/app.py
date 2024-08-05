from flask import Flask, jsonify
import random
from faker import Faker

app = Flask(__name__)
fake = Faker()


# Function to generate random data
def generate_random_data(num_records):
    data = []
    for user_id in range(1, num_records + 1):  # Sequential user IDs from 1 to num_records
        record = {
            "userId": user_id,
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "age": random.randint(18, 90),
            "address": fake.address(),
            "phoneNumber": fake.phone_number(),
            "occupation": fake.job()
        }
        data.append(record)
    return data


# Calling API GET Request to fetch data
@app.route('/api/data', methods=['GET'])
def get_data():
    num_records = 50
    random_data = generate_random_data(num_records)
    return jsonify(random_data)


if __name__ == '__main__':
    app.run(debug=True)
