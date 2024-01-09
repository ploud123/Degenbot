import client


# Read token from external file
with open("token.txt") as f:
    BOT_TOKEN = f.readline()



if __name__ == "__main__":
    client.Client().run(BOT_TOKEN)
