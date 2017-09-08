# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples – heterogenous. Fixed size
List homogenous. Dynamic

Lists can never be used as dictionaries because they are immutable. 


### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets are faster in determining if an object is present, but slower than lists when iterating over their objects.


### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lamda is an anonymous function. This function is flexible and is often used in combination with other functions. 

a = ['app','tom','dick','har','jen','ken','chris','tim','tom','mel']
c = sorted(a, key=lambda a: a)
print(c)


### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension is used to construct lists in a very natural way. 

List comprehension is a way to combine maps and filters into one statement. 

nums = [2, 7, 5, 4, 16]
## map and filter chained together 
print map(lambda x: x*2, filter(lambda y: y % 2 == 0, nums))

# equivalent version using list comprehension
print [x*2 for x in nums if x % 2 == 0]



### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





