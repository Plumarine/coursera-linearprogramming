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

s.t. food_limit {f in Foods}:
	(sum{ff in Foods}(units[ff]*costs[ff]))*0.6 >= units[f]*costs[f];

solve;

display units;
