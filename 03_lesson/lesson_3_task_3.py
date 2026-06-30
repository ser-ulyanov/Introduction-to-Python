from mailing import Mailing
from address import Address

to_address = Address(
    "101000", "Moscow", "Tverskaya street", "15", "42"
)
from_address = Address(
    "190000", "Saint Petersburg", "Nevsky Prospekt", "88", "10"
)

mailing = Mailing(to_address, from_address, 1500, "TRK987654321")

print(
    f"Mailing from {mailing.from_address.city}, "
    f"{mailing.from_address.street} {mailing.from_address.house} "
    f"to {mailing.to_address.city}, "
    f"{mailing.to_address.street} {mailing.to_address.house}. "
    f"Cost: ${mailing.cost}. Tracking number: {mailing.track}"
)
