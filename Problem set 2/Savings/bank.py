x=input("Greet me immediately: ").strip().lower()

if x.startswith("hello"):
    print("0$")
elif x.startswith("h") and not x.startswith("hello"):
    print("20$")
else:
    print("100$")