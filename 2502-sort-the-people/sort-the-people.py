class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine names and heights into a list of tuples
        people = list(zip(names, heights))
        
        # Sort people by height (in descending order)
        sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names from the sorted people list
        sorted_names = [name for name, height in sorted_people]
        
        return sorted_names
