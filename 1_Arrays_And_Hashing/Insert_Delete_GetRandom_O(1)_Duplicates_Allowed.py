"""
Insert Delete GetRandom O(1) - Duplicates allowed

Hard

RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). 
It should support inserting and removing specific elements and also reporting a random element.

Implement the RandomizedCollection class:
    RandomizedCollection() Initializes the empty RandomizedCollection object.
    bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
    bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. 
    Note that if val has multiple occurrences in the multiset, we only remove one of them.
    int getRandom() Returns a random element from the current multiset of elements. 
    The probability of each element being returned is linearly related to the number of the same values the multiset contains.
You must implement the functions of the class such that each function works on average O(1) time complexity.

Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.

Example 1:
Input
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
Output
[None, true, false, true, 2, true, 1]
Explanation
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // return true since the collection does not contain 1.
                                  // Inserts 1 into the collection.
randomizedCollection.insert(1);   // return false since the collection contains 1.
                                  // Inserts another 1 into the collection. Collection now contains [1,1].
randomizedCollection.insert(2);   // return true since the collection does not contain 2.
                                  // Inserts 2 into the collection. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should:
                                  // - return 1 with probability 2/3, or
                                  // - return 2 with probability 1/3.
randomizedCollection.remove(1);   // return true since the collection contains 1.
                                  // Removes 1 from the collection. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 or 2, both equally likely.
"""

from random import random

class RandomizedCollection:

    def __init__(self):
        """
        Initializes the data structure.
        - `hashmap`: A dictionary where keys are the values in the collection,
          and values are sets of indices where the values are stored in the `array`.
        - `array`: A list that holds the values of the collection.
        """
        self.hashmap = {}  # Maps values to sets of indices in the array
        self.array = []    # Stores the values of the collection

    def insert(self, val: int) -> bool:
        """
        Inserts a value into the collection.
        - If the value is already present in the collection, add its new index to the hashmap.
        - Append the value to the array regardless of whether it's a duplicate.
        - Returns `True` if the value was not already present, `False` otherwise.
        """
        if val not in self.hashmap:
            # If `val` is not in `hashmap`, initialize a set for it and append it to `array`.
            self.hashmap[val] = {len(self.array)}
            self.array.append(val)
            return True
        else:
            # If `val` is already in `hashmap`, add the new index to its set.
            self.hashmap[val].add(len(self.array))
            self.array.append(val)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection.
        - If the value is not in the collection, return `False`.
        - Otherwise, remove an occurrence of the value.
        - Replace the value's index with the last element of the array for efficient removal.
        - Update the hashmap accordingly.
        - Returns `True` if the value was removed, `False` otherwise.
        """
        if val not in self.hashmap:
            # If `val` is not in `hashmap`, it cannot be removed.
            return False
        else:
            # Get an arbitrary index of `val` from the hashmap.
            idx = self.hashmap[val].pop()

            # If `idx` is not the last index in the array, swap it with the last element.
            if idx != len(self.array) - 1:
                # Swap `array[idx]` with `array[-1]` (last element in the array).
                self.array[-1], self.array[idx] = self.array[idx], self.array[-1]

                # Update the hashmap for the swapped value.
                swapped_value = self.array[idx]
                self.hashmap[swapped_value].remove(len(self.array) - 1)
                self.hashmap[swapped_value].add(idx)

            # Remove the last element from the array (efficient pop operation).
            self.array.pop()

            # If the set of indices for `val` is now empty, remove it from the hashmap.
            if not self.hashmap[val]:
                self.hashmap.pop(val)
            return True

    def getRandom(self) -> int:
        """
        Returns a random value from the collection.
        - Uses the `random()` function to generate a random index.
        - Accesses the value at that index in the `array`.
        """
        return self.array[int(len(self.array) * random())]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

operations = ["RandomizedCollection", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
values = [[], [1], [2], [2], [], [1], [2], []]


# Initialize RandomizedCollection and capture output
collection = None
output = []

for op, val in zip(operations, values):
    if op == "RandomizedCollection":
        collection = RandomizedCollection()  # Initialize the collection
        output.append(None)
    elif op == "insert":
        output.append(collection.insert(val[0]))  # Insert value
    elif op == "remove":
        output.append(collection.remove(val[0]))  # Remove value
    elif op == "getRandom":
        output.append(collection.getRandom())  # Get random value

print(output)

operations2 = ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
values2 = [[], [1], [1], [2], [], [1], []]

collection2 = None
output2 = []

for op, val in zip(operations2, values2):
    if op == "RandomizedCollection":
        collection2 = RandomizedCollection()  # Initialize the collection2
        output2.append(None)
    elif op == "insert":
        output2.append(collection2.insert(val[0]))  # Insert value
    elif op == "remove":
        output2.append(collection2.remove(val[0]))  # Remove value
    elif op == "getRandom":
        output2.append(collection2.getRandom())  # Get random value

print(output2)

from random import random

class RandomizedCollection:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            self.hashmap[val].append(len(self.array))  # Append index to the list
            self.array.append(val)
            return False
        else:
            self.hashmap[val] = [len(self.array)]  # Start a new list for this value
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap or not self.hashmap[val]:
            return False
        else:
            idx = self.hashmap[val].pop()  # Get the last inserted index for val
            if idx != len(self.array) - 1:
                swapped_value = self.array[-1]
                self.array[-1], self.array[idx] = self.array[idx], self.array[-1]
                
                # Update the hashmap for the swapped value
                self.hashmap[swapped_value].remove(len(self.array) - 1)
                self.hashmap[swapped_value].append(idx)
            
            self.array.pop()
            
            if not self.hashmap[val]:
                del self.hashmap[val]  # Remove the entry if no more occurrences
            
            return True

    def getRandom(self) -> int:
        return self.array[int(len(self.array) * random())]

