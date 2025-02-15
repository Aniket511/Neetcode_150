class Solution:
    def sortArray(self, array):
        size = len(array)
        if size == 1:
            return array

        def shell_sort(array, size) -> None:
            gap = size // 2  # Initial gap
            while gap > 0:
                print(f"\n--- Sorting with gap = {gap} ---")
                for idx_1 in range(gap, size):
                    print(f"\nConsidering element {array[idx_1]} at index {idx_1}")

                    # The element to compare with
                    idx_2 = idx_1 - gap
                    while idx_2 >= 0 and array[idx_2] > array[idx_1]:
                        # Swap elements if they're in the wrong order
                        print(f"  Swapping {array[idx_2]} (index {idx_2}) and {array[idx_1]} (index {idx_1})")
                        array[idx_1], array[idx_2] = array[idx_2], array[idx_1]
                        # Move idx_1 and idx_2 back for next comparison
                        idx_1 = idx_2
                        idx_2 = idx_1 - gap

                    print(f"Array after considering index {idx_1}: {array}")

                # Reduce the gap size
                gap //= 2
                print(f"Array after gap {gap}: {array}")

        # Perform Shell Sort
        shell_sort(array, size)
        return array

# Example usage:
solution = Solution()
print("Sorted array:", solution.sortArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

class Solution:
    # Function to sort an array (entry point for the algorithm)
    def sort_array(self, array: list[int]) -> list[int]:
        """
        Main function to sort an array using merge sort.
        :param array: List of integers to be sorted.
        :return: Sorted list of integers.
        """
        # Call the merge_sort helper function on the entire array
        self.merge_sort(array, 0, len(array) - 1)
        return array

    # Function to perform merge sort on the array
    def merge_sort(self, array, start, end):
        """
        Recursive function to perform merge sort on a given range of the array.
        :param array: The list of integers to sort.
        :param start: The starting index of the subarray to sort.
        :param end: The ending index of the subarray to sort.
        """
        # Base case: If the start index is not less than the end index, no sorting is needed
        if start < end:
            print(f"Dividing array from index {start} to {end}")
            # Find the middle index to split the array into two halves
            middle = (start + end) // 2
            print(f"Middle index: {middle}")

            # Recursively sort the left half of the array
            print(f"Sorting left half from index {start} to {middle}")
            self.merge_sort(array, start, middle)

            # Recursively sort the right half of the array
            print(f"Sorting right half from index {middle + 1} to {end}")
            self.merge_sort(array, middle + 1, end)

            # Merge the sorted subarrays back into the main array
            print(f"Merging subarrays from index {start} to {end}")
            left_subarray = array[start:middle + 1]  # Elements from start to middle
            right_subarray = array[middle + 1:end + 1]  # Elements from middle+1 to end
            self.merge(left_subarray, right_subarray, array, start)

    # Function to merge two sorted subarrays into the main array
    def merge(self, left_subarray, right_subarray, main_array, start_index):
        """
        Merge two sorted subarrays into the main array.
        :param left_subarray: The sorted left subarray.
        :param right_subarray: The sorted right subarray.
        :param main_array: The original array to store the merged results.
        :param start_index: The starting index in the main array to begin merging.
        """
        left_index, right_index = 0, 0
        main_index = start_index

        # Merge elements while both subarrays have remaining elements
        while left_index < len(left_subarray) and right_index < len(right_subarray):
            if left_subarray[left_index] <= right_subarray[right_index]:
                main_array[main_index] = left_subarray[left_index]
                left_index += 1
                print(f"Placed {main_array[main_index]} from left subarray into main array.")
            else:
                main_array[main_index] = right_subarray[right_index]
                right_index += 1
                print(f"Placed {main_array[main_index]} from right subarray into main array.")
            main_index += 1

        # Copy remaining elements from the left subarray, if any
        while left_index < len(left_subarray):
            main_array[main_index] = left_subarray[left_index]
            left_index += 1
            main_index += 1
            print(f"Placed {main_array[main_index - 1]} from left subarray into main array.")

        # Copy remaining elements from the right subarray, if any
        while right_index < len(right_subarray):
            main_array[main_index] = right_subarray[right_index]
            right_index += 1
            main_index += 1
            print(f"Placed {main_array[main_index - 1]} from right subarray into main array.")

        print(f"Merged array: {main_array[start_index:main_index]}\n")

# Example usage:
solution = Solution()
print(solution.sort_array([1, 3, 5, 7, 9, 8, 4, 6, 2]))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
