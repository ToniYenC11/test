i = int(input("Strictly give me an integer that is the upper limit of the sequence"))

for i in range(0,i+1):
    to= ""
    if i%3==0:
        to+="Fizz"
    if i%5==0:
        to+="Buzz"

        if to == "":
            to=str(i)
        return to
