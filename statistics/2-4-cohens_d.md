[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

df = nsfg.ReadFemPreg()
print(df.columns)
#df.to_csv('medical.csv')

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

def CohenEffectSize(g1, g2):
	diff = g1.mean() - g2.mean()

	var1 = g1.var()
	var2 = g2.var()
	n1, n2 = len(g1), len(g2)

	pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
	d = (diff/math.sqrt(pooled_var))
	return d

weights = CohenEffectSize(g1, g2)
print(weights)
