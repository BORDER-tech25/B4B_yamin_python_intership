def build_invoice(customer_name, *prices, **details):
    print("Customer Name:", customer_name)
    print("Total Amount:", sum(prices))
    print("Extra Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

print("----- Invoice -----")

build_invoice(
    "Yamin",
    250,
    450,
    300,
    discount="10%",
    tax="18%",
    payment="UPI"
)