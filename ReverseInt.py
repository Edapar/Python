x = raw_input("What is your number?(Size Int32)")
y = [int(i) for i in str(abs(x))]
z = y[::-1]
ans = sum(d *10**i for i, d in enumerate(z[::-1]))
if ans.bit_length() < 32:
    if x == abs(x):
        print("The reverse of your number is ", ans)
    else:
        print("The reverse of your number is ",-ans)
else:
    print("The number is out of int32 range, returning 0")




