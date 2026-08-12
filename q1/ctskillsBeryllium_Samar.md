Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: _____________9-Beryllium____________ Score:____________

C# / Name:______Ian______ Date: ___8/14/26____


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: ___During lunch break, some students take too long to decide what to order, as
the cashier has to manually calculate totals and give change, and 
there is no system to track which food items are running out._____

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. _Some students take too long to decide what to order_____
_____________________________________________________________

2. _The cashier has to manually calculate totals and give change______
_____________________________________________________________

3. _There is no system to track which food items are running out____
_____________________________________________________________

4. _The process of getting food is slow.______
_____________________________________________________________

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

  **Sub-Problem 1:**
CT Skill: Pattern Recognition

Example Solution: 
- By finding a trend or a pattern to the students' choice of food, inputting the choices of the customers can be faster to be typed.

  **Sub-Problem 2:**
CT Skill: Automation

Example Solution:
- When there is a set of items with their corresponding prices, having a machine can automate this process, increasing efficiency by a lot.

  **Sub-Problem 3:**
CT Skill: Algorithm

Example Solution:
- An algorithm is to be constructed where desired food items and its quantity is an input, which the machine can process this to output a receipt and the exact amount of change to be given back to the student.

  **Sub-Problem 4:**
CT Skill: Optimization

Example Solution:
- From the solution to the 3 sub-problems, we can optimize speed and efficiency of the program, by for example, predicting the food item: when a food item is typed half-way like "Ri", we can say that it is "Rice".



 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
**Pseudocode** (Sub-problem 3 = Algorithm):

INPUT food item, quantity of food item
food_prices: 
 Rice: 12
 Pork: 50
 Chicken: 40

total_cost = food item price * quantity of food item

INPUT given money
change = total_cost - money

PRINT total_cost
PRINT change

