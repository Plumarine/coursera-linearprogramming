set Foods;
set Nutrients; 

param costs{Foods};
param foodNutrients{Foods, Nutrients};
param lowerNutrients{Nutrients};
param upperNutrients{Nutrients};

var units{Foods} >= 0;

maximize obj: sum{f in Foods}(units[f]*foodNutrients[f, 'Proteins']);

s.t. bounds {n in Nutrients}:
	lowerNutrients[n] <= sum{f in Foods}(units[f]*foodNutrients[f,n]) <= upperNutrients[n];

s.t. price_limit:
	sum{f in Foods}(units[f]*costs[f]) <= 2;

solve;

display units;
