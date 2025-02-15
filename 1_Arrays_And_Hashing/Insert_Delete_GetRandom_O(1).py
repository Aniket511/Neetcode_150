"""
Insert Delete GetRandom O(1)

Medium

Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements 
    (it's guaranteed that at least one element exists when this method is called). 
    Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""

from random import random  # Importing the random function to generate a random number
class RandomizedSet:
    def __init__(self):
        """Initialize the RandomizedSet."""
        self.hashmap = {}  # A dictionary (hashmap) to store the value as the key and its index in the list as the value
        self.array = []  # A list to store the values, which allows for O(1) random access

    def insert(self, val: int) -> bool:
        """
        Insert a value into the set. If the value already exists, return False.
        Otherwise, add the value to the list and map its index to the dictionary.
        
        :param val: The value to insert
        :return: True if the value was inserted, False if it was already present.
        """
        if val in self.hashmap:  # Check if the value already 
            return False  # If it exists, return False

        self.array.append(val)  # Add the value to the end of the list
        self.hashmap[val] = len(self.array) - 1  # Map the value to its index in the list (0-based index)
        return True  # Successfully inserted, return True

    def remove(self, val: int) -> bool:
        """
        Remove a value from the set. If the value does not exist, return False.
        Otherwise, remove the value and update the mapping to keep track of the list's current state.
        
        :param val: The value to remove
        :return: True if the value was removed, False if it was not found.
        """
        if val not in self.hashmap.keys():
            return False
        else:
            idx = self.hashmap[val]
            if idx != len(self.array) - 1:
                swapped_value = self.array[-1]
                self.array[-1], self.array[idx] = self.array[idx], self.array[-1]
                self.hashmap[swapped_value] = idx
            self.array.pop()
            del self.hashmap[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        :return: A random value from the set.
        """
        # Use the random function to generate a random index and return the corresponding element from the list
        return self.array[int(random() * len(self.array))]  # int() ensures we get an integer index
