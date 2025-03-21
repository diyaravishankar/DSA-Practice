from collections import deque
class Solution:
 def findAllRecipes(self, recipes, ingredients, supplies):
  graph = {recipe: [] for recipe in recipes}
  in_degree = {recipe: 0 for recipe in recipes}
  available = set(supplies)
  for i, recipe in enumerate(recipes):
   for ingredient in ingredients[i]:
    if ingredient not in available:
     graph.setdefault(ingredient, []).append(recipe)
     in_degree[recipe] += 1
  queue = deque([recipe for recipe in recipes if in_degree[recipe] == 0])
  result = []
  while queue:
   recipe = queue.popleft()
   result.append(recipe)
   available.add(recipe)
   for dependent in graph[recipe]:
    in_degree[dependent] -= 1
    if in_degree[dependent] == 0:
     queue.append(dependent)
  return result