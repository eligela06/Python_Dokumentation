username = input("Input your Username: ")

username_len = len(username) >= 5
username_space = " " in username
username_at = "@" in username
username_admin = username.startswith("admin")

if (
    username_len == False 
    and username_space == False 
    and username_at == False 
    and username_admin == False
    ):
    print("Username valid")
else:
    print("Username invalid")