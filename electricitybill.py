import sys

if len(sys.argv) != 2:
    print("Usage: python electricity_bill.py <units>")
    sys.exit(1)

units = float(sys.argv[1])
bill = units * 5

print("Electricity Bill: ₹", bill)
