[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

df = pd.DataFrame(np.zeros((1000,1)), columns=['Random'])

for i in range(0,999):
	df.iloc[i,0] = np.random.normal(0,1)
  
# Plot the PDF
df.plot(kind='hist', bins=30, range=(-5,5))
plt.xlabel('Time (in seconds)')
plt.ylabel('Bits of Ham')
plt.show()

# Plot the CDF
df.plot(kind='hist', cumulative=True, bins=30, range=(-5,5))
plt.xlabel('Time (in seconds)')
plt.ylabel('Bits of Ham')
plt.show()
