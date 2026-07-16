def make_greeting(language):

    def greet(name):
        if language.lower() == "english":
            print(f"Hello, {name}")
        elif language.lower() == "hindi":
            print(f"Namaste, {name}")
        else:
            print(f"Hi, {name}")

    return greet

english = make_greeting("english")
hindi = make_greeting("hindi")

english("Yamin")
hindi("Rahul")