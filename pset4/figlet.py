from pyfiglet import Figlet
import sys

figlet = Figlet()

#check for argument length
if len(sys.argv) == 3 or len(sys.argv) == 1:

    f = sys.argv[2]
    #check for second argument
    if not sys.argv[1] in ["-f", "--font"]:
        sys.exit("Invalid Usage")
    #check for valid font name
    if not sys.argv[2] in figlet.getFonts():
        sys.exit("Invalid Usage")
    #take input
    input = input("input: ")

    if len(sys.argv) == 3:
        figlet.setFont(font=f)
        print(figlet.renderText(input))

    else:
        print(figlet.renderText(input))

else:
    sys.exit("Invalid Usage")

