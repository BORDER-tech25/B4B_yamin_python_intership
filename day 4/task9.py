def update_status():
    status = "pending"

    def complete():
        nonlocal status
        status = "completed"

    complete()
    print("Final Status:", status)

update_status()
