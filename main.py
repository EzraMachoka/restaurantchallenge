# Import the classes from the respective files
from customer import Customer
from restaurant import Restaurant
from review import Review

# Create customers and restaurants
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Delicious Eats")
restaurant2 = Restaurant("Tasty Treats")

# Add reviews
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)

# Example usage
print(customer1.full_name())            # Output: John Doe
print(Restaurant.all_restaurants())       # Output: [restaurant1, restaurant2]
print(review1.rating())                 # Output: 4
print(restaurant1.customers())          # Output: [customer1, customer2]
print(restaurant1.average_star_rating())  # Output: 4.5

# Exit the Python interpreter
exit()
