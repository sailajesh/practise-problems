"""tip calculator"""
print("""welcome to the tip calculator""")
bill=float(input("what was the total bill "))
tip=int(input("what is the tip would u like to give? 10,12 or 15? "))
persons=int(input("total number of persons? "))
tip_convert=tip / 100
split=((bill*tip_convert)+bill)/persons
print(round(split,2))
print(tip_convert)