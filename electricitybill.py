import sys

if len(sys.argv) != 2:
    print("Usage: python electricity_bill.py <units>")
    sys.exit(1)

units = float(sys.argv[1])
bill = units * 5

# Encode output to UTF-8 and write directly to stdout
output = f"Electricity Bill: ₹ {bill}"
sys.stdout.buffer.write((output + "\n").encode('utf-8'))
