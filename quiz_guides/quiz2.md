# Quiz 2

The second quiz will be held **in lab on Tuesday, 3/7**.  The topic will be SQL (Lectures 5 and 6 and Lab 3).  Topics such as statistics, probability, etc. will *not* be on the quiz.

Lab 3 is a good study guide.  If you want additional practice, you can use the queries below.  They are written for a database that is defined in a [file](pizza_create.sql) called `pizza_create.sql`.  You can set up a database for it following the instructions from Lab 3 (create a database and then populate it with schema and data from `pizza_create.sql`)

1. Find pizzerias that serve pepperoni or cheese pizza, ordered by price from least expensive to most expensive.  The result should include the name of the pizzeria, the kind of pizza, and the price. 
2. Straw Hat is having a sale of 10% off all pizzas.  Write a query that returns a list of Straw Hat's pizzas and their prices, with the prices updated to reflect the sale.  Name the updated price column "saleprice." 
3. Find pizzerias that have the word Pizza in their name.  Each name should appear only once. 
4. Find the name of the most expensive pizza.  Your query should return a table with a single row and a column that contains the name of the most expensive pizza served. 
5. Find the names of pizzerias that serve pizzas that cost under \$9 and are either pepperoni or cheese.  The result should include only the name of the pizzeria and duplicate names should be eliminated. 
6. Are there pizzerias that serve pizzas that Dan likes to eat for under \$8?  Write a query that returns the pizza, the pizzeria where it's served, and the price of the pizza at that pizzeria.  (Note: Dan may not necessarily frequent this pizzeria.) 
7. Names of people together with the pizzas they like to eat along with where they like to eat it.   
8. Find the names of all females who eat at least one pizza served by Straw Hat. (Note: The pizza need not be eaten at Straw Hat.) 
9. Find pairs of pizzerias who sell the same kind of pizza for the same price.  The result should include both the names of both pizzerias along with the pizza and the price. 
10. Find all pizzas either Amy or Fay (or both) eat. 
11. Find all pizzas that both Amy and Fay eat.  Hint: this is harder than it looks. 
12. Find the price of the most expensive pizza served by Pizza Hut. 
13. Find the age of the oldest person (or people) who eat mushroom pizza. 
14. Find the price of the most expensive pizza served by each pizzeria. 
15. Find the number of pizzas made by each pizzeria 
16. Find the number of distinct kinds of pizza eaten by each gender. 
17. Find the names of pizzerias who serves at least 4 kinds of pizza. 
18. Find the average number of pizzas made by a pizzeria.  Hint: first do a subquery that computes the number of pizzas made by each pizzeria. 
19. Find the average number of pizza kinds eaten by each gender.  Hint: use the WITH keyword to create a table called pizzaCounts with attributes name, gender and numPizzas where numPizzas is the number of types pizzas that person eats.  Then issue a query on this new table. 
20. Find the names of people who frequent at least three pizzerias that serve pizzas that they eat.  This is a challenging query.  The final answer should include the person named Hil (and in fact only Hil).  Hil frequents Dominos, Pizza Hut, and Straw Hut and each of those establishes serves at least one pizza that Hil eats (specifically, cheese, though Pizza Hut also serves supreme). 
