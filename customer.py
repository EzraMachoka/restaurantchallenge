# customer.py
from review import Review
class Customer:
    _all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer._all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls._all_customers

    def restaurants(self):
        reviewed_restaurants = set()
        for review in self._reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls._all_customers:
            if customer.given_name() == name:
                matching_customers.append(customer)
        return matching_customers
