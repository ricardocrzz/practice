Quick Sort

__________

6270143958

Pivot=4
     4
62701_3958 
Compare with 6
4
62701_3958
Compare with 2
 4
62701_3958
Hold 2
24
6_701_3958
Go to end and compare with 8
2        4
6_701_3958
Place 8 where 2 was and place 2 where 8 was
 4
68701_3952
Compare with 7
  4
68701_3952
Compare with 0
   4
68701_3952
Hold 0
0  4
687_1_3952
Hold 0
0  4
687_1_3952
Go to end and compare with 5
0       4
687_1_3952
Place 5 where 0 was and place 0 where 5 was
   4
68751_3902
Compare with 1
    4
68751_3902
Hold 1
1   4
6875__3902
Go to end and compare with 9
1      4
6875__3902
Place 9 where 1 was and place 1 where 9 was
    4
68759_3102
Compare with 3
      4
68759_3102
Place 4 down permanently
     *
6875943102

Pivot=1
     * 1
6875943_02
Compare with 3
     *1
6875943_02
Compare with 0
     *  1
6875943_02
Hold 0
     *0 1
6875943__2
Go to end and compare with 2
     *0  1
6875943__2
Swap 0 and 2
     *   1
68759432_0
Place 1 and 0 down permanently
     *  **
6875943210

Pivot=3
     *3 **
687594_210
Compare with 2
     * 3**
687594_210
Place 3 and 2 down permanently
     *****
6875943210

Pivot=7
  7  *****
68_5943210
Compare with 6
7    *****
68_5943210
Hold 6
6
7    *****
_8_5943210
Go to end and compare with 9
6   7*****
_8_5943210
Swap 9 and 6
7    *****
98_5643210
Compare with 8
 7   *****
98_5643210
Compare with 5
   7 *****
98_5643210
Place 7 down permanently
  *  *****
9875643210

Pivot=5
  *5 *****
987_643210
Compare with 6
  * 5*****
987_643210
Place 5 and 6 down permanently
  ********
9876543210

Pivot=9
9 ********
_876543210
Compare with 8
 9 ********
_876543210
Place 9 and 8 down permanently
**********
9876543210
Array sorted.

Steps:
1- Select Pivot
2- Compare Pivot to most left value in unsorted section
    if current left value is less than pivot
        put current left value down 
        move on to value on the right of the current left value
    else
        hold value
        compare pivot to most right value in unsorted section
        if value is more than pivot
            keep in place and move on the next most right value