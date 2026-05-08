from mailing import Mailing
from address import Address

mailing = Mailing(
    "16 Energetikov street",
    "17 Energetikov street",
    1000,
    "TRACK12345",
)
print(
    f"Mailing from {mailing.from_address} to {mailing.to_address}. "
    f"Cost: ${mailing.cost}. Tracking number: {mailing.track}"
)

address = Address("625034", "Tyumen", "Energetikov street", "16", "A")
print(
    f"Address: {address.zip_code}, {address.city}, {address.street}, "
    f"{address.house}, {address.apartment}"
)
