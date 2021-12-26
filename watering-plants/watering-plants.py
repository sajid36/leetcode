class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp_capacity = capacity
        steps = 0
        for i in range(len(plants)):
            #print(i)
            if(plants[i] <= temp_capacity):
                steps = steps + 1
                temp_capacity = temp_capacity - plants[i]
                #print("if step", steps) 
            else:
                steps = steps + i + i + 1
                temp_capacity = capacity  - plants[i]
                #print("eif step", steps)

        return (steps) 
        