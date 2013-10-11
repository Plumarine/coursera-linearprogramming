var x{0 .. 3} >= 0;

maximize Objective: -x[0];

s.t. c1: -x[1] -x[2]	 		-x[0] <= 5;
s.t. c2:  x[1] -2*x[2]	 +x[3] 	-x[0] <= -10;
s.t. c3:  x[1]			 -x[3]	-x[0] <= -20;
s.t. c4:  x[1] +x[2]	 +x[3]	-x[0] <= 3;

solve;
display x;
