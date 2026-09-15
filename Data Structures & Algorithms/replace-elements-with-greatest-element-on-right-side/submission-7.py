class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = -1
        for i in range(len(arr) - 1, -1, -1):
            current_val = arr[i]
            arr[i] = max_element
            
            if current_val > arr[i]:
                max_element = current_val
        return arr