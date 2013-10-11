set Foods;
set Nutrients; 

param costs{Foods};
param foodNutrients{Foods, Nutrients};
param lowerNutrients{Nutrients};
param upperNutrients{Nutrients};

var units{Foods} >= 0;

minimize obj: sum{f in Foods}(units[f]*costs[f]);

s.t. bounds {n in Nutrients}:
	lowerNutrients[n] <= sum{f in Foods}(units[f]*foodNutrients[f,n]) <= upperNutrients[n];

solve;

display units;
