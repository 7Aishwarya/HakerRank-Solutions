/*
We use the integers a, b, and n to create the following series:
(a+2^0.b),(a + 2^0.b+2^1.b),...,(a + 2^0.b+2^1.b+...+2^(n-1).b)

You are given  queries in the form of a, b, and n. For each query, print the series corresponding to 
the given a, b, and n values as a single line of n space-separated integers.
*/


import java.util.*;
import java.io.*;
import java.lang.Math;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        int j, power, product, sum;
        for(int i=0;i<t;i++){
            sum = 0;
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            for(j=0; j<n; j++)
            {
                power = (int)Math.pow(2,j);
                product = power * b;
                sum = sum + product;
                System.out.print(a + sum + " ");
            }
            System.out.println();
        }
        in.close();
    }
}

