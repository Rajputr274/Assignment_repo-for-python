import pymysql

# first we Connect to MySQL
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="724857"
)

# Make a cusror connection

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS product_db")
print("Database created successfully.")

cursor.execute("USE product_db")
print("Database selected.")


cursor.execute("""
CREATE TABLE IF NOT EXISTS product_table(
    id INT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    category VARCHAR(100),
    price DECIMAL(10,2),
    discountPercentage FLOAT,
    rating FLOAT,
    stock INT,
    tags VARCHAR(255)
)
""")

print("Table created successfully.")

product = {
    "id": 1,
    "title": "Essence Mascara Lash Princess",
    "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
    "category": "beauty",
    "price": 9.99,
    "discountPercentage": 7.17,
    "rating": 4.94,
    "stock": 5,
    "tags": ["beauty", "mascara"]
}

query = """
INSERT INTO product_table
(id, title, description, category, price,
discountPercentage, rating, stock, tags)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


tags = ",".join(product["tags"])

values = (
    product["id"],
    product["title"],
    product["description"],
    product["category"],
    product["price"],
    product["discountPercentage"],
    product["rating"],
    product["stock"],
    tags
)


cursor.execute("SELECT * FROM product_table WHERE id=%s", (product["id"],))

if cursor.fetchone() is None:
    cursor.execute(query, values)
    mydb.commit()
    print("Product inserted successfully.")
else:
    print("Product already exists.")


cursor.execute("SELECT * FROM product_table")

print("\nProducts:\n")

for row in cursor.fetchall():
    print(row)

# Close Connection
cursor.close()
mydb.close()