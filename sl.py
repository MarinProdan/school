i= 1
is_sep=False
while i < 10:
    if is_sep:
        print("-", end="")
    else:
        is_sep=True
    print(i, end="")
    i+=1
    if i == 7:
        break