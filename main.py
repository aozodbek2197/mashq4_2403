# 7-mashq
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = max(speed, 0)

cars = [
    Car("Toyota", 180),
    Car("BMW", 220),
    Car("Ferrari", 350),
    Car("Tesla", 250),
    Car("Lada", 140)
]

fastest = max(cars, key=lambda c: c.speed)
print(f"Eng tez mashina: {fastest.brand} ({fastest.speed} km/h)")

avg_speed = sum(c.speed for c in cars) / len(cars)
print(f"O'rtacha tezlik: {avg_speed:.1f} km/h")
# 8-mashq
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades.values()) / len(self.grades)

    def passed(self):
        return self.average() >= 60

students = [
    Student("Ali", {"Math": 85, "Phys": 90, "Chem": 78}),
    Student("Vali", {"Math": 55, "Phys": 60, "Chem": 45}),
    Student("Soli", {"Math": 95, "Phys": 88, "Chem": 92}),
    Student("Guli", {"Math": 70, "Phys": 75, "Chem": 80}),
    Student("Dilorom", {"Math": 40, "Phys": 50, "Chem": 55})
]

for s in students:
    print(f"{s.name}: o'rtacha {s.average():.1f}")

passed_students = [s for s in students if s.passed()]
print(f"O'tgan talabalar: {[s.name for s in passed_students]}")
# 9-mashq
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self):
        return self.price

products = [
    Product("Noutbuk", 12000000),
    Product("Telefon", 8500000),
    Product("Quloqchin", 1200000),
    Product("Monitor", 4500000),
    Product("Klaviatura", 800000)
]

total = sum(p.total_price() for p in products)
print(f"Barcha mahsulotlarning umumiy narxi: {total:,} so'm")

most_expensive = max(products, key=lambda p: p.price)
print(f"Eng qimmat mahsulot: {most_expensive.name} ({most_expensive.price:,} so'm)")
