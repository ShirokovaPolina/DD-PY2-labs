infV_Mb = 1.44
infV_Kb = infV_Mb * 1024
infV_bite = infV_Kb * 1024
pages = 100
strings = 50
symbols_in_string = 25
symV_bite = 4
stringV = symbols_in_string * symV_bite
pageV = stringV * strings
bookV = pageV * pages
count_of_books = infV_bite / bookV
print(f"Количество книг, помещающихся на дискету: {count_of_books:.0f}")
