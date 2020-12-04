import os
import httpagentparser

# chane title
os.system("title Simple User Agent parser")


print("""

Mohanjot User Agent Parser | By King Herod

           Input User Agent

""")

agent = input(">")

# parse user agent
parser = httpagentparser.detect(agent)
print("\nParsed User Agent successfully\n\nLogged information to parser.txt\n\n")

#log to text file
f = open("parser.txt", "w")
f.write(str(parser))
f.close()

os.system("pause")

