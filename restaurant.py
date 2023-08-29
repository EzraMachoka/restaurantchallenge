class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating() for review in self.reviews)
        return total_ratings / len(self.reviews)


# Example usage
restaurant1 = Restaurant("Delicious Eats")
restaurant2 = Restaurant("Tasty Treats")
