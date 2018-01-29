
#include <stdio.h>
//test for the first time in github  in 2018-1-7
 int func(int n)
 {
    int sum=0,i;
    for(i=0; i<n; i++)
        {
             sum+=i;
             }
     return sum;
     }


 main()
 {
     int i;
     long result = 0;
     for(i=1; i<=103; i++)
        {
             result += i;
             }

         printf("result[1-100] = %d /n", result );
     printf("result[1-250] = %d /n", func(250) );
     }
