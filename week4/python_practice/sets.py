
# ----------------------------------------------------------------------------------------------------------------------------
# Immutable sets
# -----------------------------------------------------------------------------------------------------------------------------
"""
s1.add(frozenset(s2)
fs1 = frozenset(s1)"""
# ----------------------------------------------------------------------------------------------------------------------------
# Set
# -----------------------------------------------------------------------------------------------------------------------------

"""Method                       Operators           Description

len(s)                                              Returns the number of elements in s

s.copy()                                            Returns a shallow copy of s

s.difference(t)                 s - t- t2 - ...     Returns a set of all items in s but not in t

s.intersection(t)                                   Returns a set of all items in both t and s

s.isdisjoint(t)                                     Returns True if s and t have no items in common

s.issubset(t)                   s <= t              Returns True if all items in s are also in t
                                s < t (s != t)

s.issuperset(t)                 s >= t              Returns True if all items in t are also in s
                                s > t (s != t)


s.symmetric_difference(t)       s ^ t               Returns a set of all items that are in s or t, but not both

s.union(t)                      s | t1 | t2 |...    Returns a set of all items in s or t """


"""Method                                           Description

s.add(item)                                         Adds item to s. Has no effect if item is already present.

s.clear()                                           Removes all items from s.

s.difference_update(t)                              Removes all items in s that are also in t.

s.discard(item)                                     Removes item from s.

s.intersection_update(t)                            Removes all items from s that are not in the intersection of s and t.

s.pop()                                             Returns and removes an arbitrary item from s.

s.remove(item)                                      Removes item from s.

s.symetric_difference_update(t)                     Removes all items from s that are not in the symmetric difference of s and t.

s.update(t)                                         Adds all the items in an iterable object t to s."""

#In a Set, items are unordered, unindexed and do not allow duplicate values.

#Unordered means that the items in a set do not have a defined order.

#This means that items in a Set can appear in a different order every time you use them, and cannot be referenced by an index or key.

#Sets cannot have two items with the same value.

#A Set is created by placing a sequence of values separted by a comma inside curly brackets {}


progLang = {"python", "c#", "javascript", "java", "c++"}
moreLang = {"rust", "php", "perl", "ruby", "go", "java", "python"}

myNumbers = {1,2,3,4,5}

myFloats = {1.0, 2.1, 3.2, 4.3}

progLang.add("HTML") # No Duplicate Error (does not allow duplicate values)
print(progLang)

removedItem = progLang.pop() # Removes Random
print(progLang)
print(removedItem)

progLang.discard("c#")
print(progLang)

# progLang.remove("c#") # Throw Error if Item is not in the Set
print(progLang)

print(progLang.difference(moreLang)) # Values not shared
print(progLang)

print(progLang.intersection(moreLang)) # Values shared




# --------------------------------------------------------------------------------------------------------------------------