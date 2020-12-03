import os
import httpagentparser


os.system("title Simple User Agent parser")


print("""

Mohanjot User Agent Parser | By King Herod

           Input User Agent

""")

agent = input(">")

parser = httpagentparser.detect(agent)
print("\nParsed User Agent successfully\n\nLogged information to parser.txt\n\n")


f = open("parser.txt", "w")
f.write(str(parser))
f.close()

os.system("pause")

