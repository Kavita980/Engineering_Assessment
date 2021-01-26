# Engineering_Assessment
LRU Cache Implementation in python

This python file demonstrate the construction of Least Recently Used (LRU) cache.

A Least Recently Used (LRU) Cache organizes items in order of use, allowing you to quickly identify which item hasn't been used for the longest amount of time. To implement this idea I ahve used the doubly linked list (DLL) and a hash-map.

In this implementation LRU Cache will be initialised with the fix maximum amount of size and after then DLL will set up with the most recently used item at the head and least recently used item at the end which allows the access of the LRU element in O(1) time.

But when we look for a specific item then traversal of the DLL will take O(n) time and to get the quick lookups, we can implement hash-maps which maps the items to the DLL. Hence, to look up any element into the DLL or cache takes O(1) time, instead of O(n).

Hence, the whole idea of combining Hash-maps and Doubly Linked List (DLL) can be treated as the Least Recently Used (LRU) Cache.
