import sys
import random
import argparse
import pyfiglet
 
 
def main():
    parser = argparse.ArgumentParser(description="FIGlet ASCII art generator")
    parser.add_argument("-f", "--font", metavar="FONT", help="FIGlet font name")
    args = parser.parse_args()
 
    available_fonts = pyfiglet.FigletFont.getFonts()
 
    if args.font is not None:
        if args.font not in available_fonts:
            sys.exit(f"Invalid font: '{args.font}'. Choose from available FIGlet fonts.")
        font = args.font
    else:
        font = random.choice(available_fonts)
 
    text = input("Input: ")
    print(pyfiglet.figlet_format(text, font=font))
 
 

main()