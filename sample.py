from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb+srv://123:123@cluster0.kdydgz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Update with your MongoDB URI
db = client['license_plate_db']
collection = db['plates']

# Sample data
sample_data = [
    { "plate_number": "ABC1234", "owner_name": "John Doe", "vehicle_model": "Toyota Camry", "registration_date": "2023-05-10T10:00:00Z" },
    { "plate_number": "XYZ5678", "owner_name": "Jane Smith", "vehicle_model": "Honda Accord", "registration_date": "2023-04-15T09:30:00Z" },
    { "plate_number": "LMN9101", "owner_name": "Alice Brown", "vehicle_model": "Ford Focus", "registration_date": "2023-03-20T14:20:00Z" },
    { "plate_number": "MH12DE1433", "owner_name": "Dev", "vehicle_model": "Ford ENdevor", "registration_date": "2024-03-20T14:20:00Z" }
]

# Insert sample data into the collection
collection.insert_many(sample_data)

print("Sample data inserted successfully")
