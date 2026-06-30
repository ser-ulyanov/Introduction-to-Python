from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 12", "+1234567890"),
    Smartphone("Samsung", "Galaxy S23", "+0987654321"),
    Smartphone("Xiaomi", "Mi 11", "+1122334455"),
    Smartphone("Google", "Pixel 7", "+5566778899"),
    Smartphone("Nokia", "3310", "+9988776655")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
