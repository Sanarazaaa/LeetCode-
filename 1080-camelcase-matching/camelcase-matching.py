class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []  # To store the results for each query
        for query in queries:
            pos1 = 0  # Pointer for the query
            pos2 = 0  # Pointer for the pattern
            match = True  # Flag to check if the current query matches the pattern
            
            while pos1 < len(query) and pos2 < len(pattern):
                if query[pos1] == pattern[pos2]:  # Characters match, move both pointers
                    pos1 += 1
                    pos2 += 1
                elif query[pos1].islower():  # Lowercase characters in query can be ignored
                    pos1 += 1
                else:  # Mismatch found and query[pos1] is uppercase, which cannot be skipped
                    match = False
                    break

            # After the loop, check if we have matched the entire pattern
            if pos2 == len(pattern):  # If we have reached the end of the pattern
                # Ensure remaining characters in the query are lowercase
                while pos1 < len(query):
                    if not query[pos1].islower():  # If any remaining character is uppercase, it's invalid
                        match = False
                        break
                    pos1 += 1

            else:  # If we didn't match the entire pattern
                match = False

            result.append(match)  # Append the result of the current query
            
        return result

