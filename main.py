
import random
import string
import webbrowser

CHARS = string.ascii_lowercase + string.digits

def generate_usernames(count=100):
    usernames = set()

    while len(usernames) < count:
        letters = random.sample(string.ascii_lowercase, 2)
        digit = random.choice(string.digits)

        username = ''.join(
            random.sample(letters + [digit], 3)
        )
        usernames.add(username)

    return sorted(usernames)

def save_results(usernames):
    with open("usernames.txt", "w") as file:
        file.write("\n".join(usernames))

def main():
    count = int(input("Number of usernames: "))

    usernames = generate_usernames(count)

    print("\nGenerated usernames:\n")

    for username in usernames:
        print(username)

    save_results(usernames)

    print("\nSaved to usernames.txt")

if __name__ == "__main__":
    main()
  
