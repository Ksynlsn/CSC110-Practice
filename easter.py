def isItEaster(year):
    year = int(input("Enter a year between 1900 and 2099"))
    if (year >= 1900 and year <= 2099):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        dateOfEaster = 22 + d + e
        if (year == 1954 or year == 1981 or year == 2049 or year == 2075):
            dateOfEaster = dateOfEaster - 7
        if (dateOfEaster > 31):
            print('April', dateOfEaster - 31, year)
        else:
            print('March', dateOfEaster, year)
    else:
        print('Select a year within the range provided')
        
  
    

isItEaster(2023)
    
