print("\n----- Valid Usernames -----")
usernames = ["sam", "yamin25", "john", "python123", "alex12"]
valid_users = list(filter(lambda name: len(name) >= 6, usernames))
print(valid_users)
