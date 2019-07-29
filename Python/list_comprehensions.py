'''Let's learn about list comprehensions! You are given three integers x, y and z representing 
the dimensions of a cuboid along with an integer n. You have to print a list of all possible 
coordinates given by (i,j,k) on a 3D grid where the sum of is not equal to i+j+k. 
Here, 0<=i<=x; 0<=j<=x; 0<=i<=x
Sample Input 
1
1
1
2
Sample Output 
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

'''


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list1 = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if((i+j+k)!=n):
                    l = [i,j,k]
                    list1.append(l)
    print(list1)