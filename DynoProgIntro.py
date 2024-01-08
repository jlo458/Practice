# This is an introductory program to dynamic programming - this is known as the knapsack problem
# I steal a group of items and find which combination of items is most profitable to steal, but I can only fit 4lbs into my bag  

itemCosts = {} 
itemCosts["Guitar"] = 1500
itemCosts["Stereo"] = 3000
itemCosts["Laptop"] = 2000

itemWeights = {} 
itemWeights["Guitar"] = 1
itemWeights["Stereo"] = 4
itemWeights["Laptop"] = 3 

columns = 0
for i in itemWeights.values():
  if i > columns: 
    columns = i

rows = len(itemCosts) 

grid = []
for _ in range(rows):  
  list = [] 
  for _ in range(columns): 
    list.append(0)

  grid.append(list)



i = 0 
for item in itemCosts:
  row = i+1
  for j in range(columns):
    column = j+1 
    newWeight = itemWeights[item]
    if newWeight <= column: 
      if i > 0: 
        newWeight = column-newWeight
        totalCost = itemCosts[item] + grid[i][newWeight-1]
        if totalCost > grid[i-1][j]:
          grid[i][j] = totalCost 
  
        else: 
          grid[i][j] = grid[i-1][j] 

      else: 
        grid[i][j] = itemCosts[item]

    else: 
      grid[i][j] = grid[i-1][j]
  i+=1
print(grid)

