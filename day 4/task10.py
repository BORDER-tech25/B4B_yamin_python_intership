mode = "Global Mode"

def outer():
    mode = "Outer Mode"
    print("Outer:", mode)

    def inner():
        mode = "Inner Mode"
        print("Inner:", mode)

    inner()
    print("Outer After Inner:", mode)

outer()
print("Global:", mode)
