# Enter your code here. Read input from STDIN. Print output to STDOUT
l1 = input().split()
Da = int(l1[0])
Ma = int(l1[1])
Ya = int(l1[2])
l2 = input().split()
De = int(l2[0])
Me = int(l2[1])
Ye = int(l2[2])
if Ya > Ye:
    fine = 10000
elif Ya < Ye:
    fine = 0
else:
    if Ma > Me:
        d = Ma - Me
        fine = 500 * d
    elif Ma < Me:
        fine = 0    
    else:
        if Da > De:
            d = Da - De
            fine = 15 * d
print(fine)


