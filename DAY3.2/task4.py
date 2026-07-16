subscribers = {
    "alice@email.com",
    "bob@email.com",
    "charlie@email.com",
    "david@email.com"
}

customers = {
    "bob@email.com",
    "charlie@email.com",
    "eva@email.com"
}

never_purchased = subscribers - customers
not_subscribed = customers - subscribers

print("Subscribers who never purchased:", never_purchased)
print("Customers who never subscribed:", not_subscribed)
