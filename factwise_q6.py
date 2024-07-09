def count():
    ones= [0,3,3,5,4,4,3,5,5,4]
    teens=[3,6,6,8,8,7,7,9,8,8]
    tens=[0,0,6,6,5,5,5,7,6,6]
    total_letters=0
    for i in range(1,1000):
        hundreds = i//100
        tens_units = i % 100
        if hundreds > 0:
            total_letters += ones[hundreds]+7
            if tens_units >0:
                total_letters +=3
        if tens_units < 10:
            total_letters += ones[tens_units]
        elif tens_units <20:
            total_letters += teens[tens_units-10]
        else:
            total_letters += tens[tens_units//10]
            if tens_units % 10>0:
                total_letters += ones[tens_units % 10]
    total_letters +=11
    return total_letters

if __name__=="__main__":
    total_letters = count()
    print(total_letters)