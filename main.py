# Functional Prompt
def flatten_and_sort(arrays):
    # Using a lambda function for the key in sorted to sort based on the values
    return sorted([item for sublist in arrays for item in sublist])

# Example usage:

nested_arrays = [[3, 1, 4], [1, 5, 9], [2, 6, 5, 3, 5]]

result = flatten_and_sort(nested_arrays)

print(result)

# How does this solution ensure data immutability?

# In this functional solution:

# The flatten_and_sort function does not modify the input arrays parameter. Instead, it creates a new list through list comprehension.
# The sorted function, used to sort the flattened list, also creates a new sorted list without modifying the original list.
# Therefore, the solution ensures data immutability by creating new data structures rather than modifying existing ones.

# Is this solution a pure function? Why or why not?

# Yes, the flatten_and_sort function is a pure function because:

# It depends only on its input parameters (arrays).
# It does not have any side effects.
# For the same input, it will always produce the same output.
# There are no external dependencies or modifications to state outside the function, making it purely based on its inputs and deterministic in its behavior.

# Is this solution a higher-order function? Why or why not?

# No, the flatten_and_sort function is not a higher-order function. A higher-order function is a function that takes one or more functions as arguments or returns a function as its result. The flatten_and_sort function only takes a list of arrays as its argument and does not operate on functions as parameters.

# Would it have been easier to solve this problem using a different programming style?

# The choice of programming style depends on various factors, including the specific requirements of the problem, the language being used, and the preferences of the programmer. For this particular problem, a functional style is well-suited, and the solution is concise and readable.

# In Python, functional programming features are often used alongside other programming paradigms, and the provided solution leverages the functional capabilities of list comprehensions and the sorted function. While it's possible to solve the problem using other programming styles, the functional approach is concise and aligns well with the nature of the task.

# Why is functional programming a helpful paradigm when solving this problem?

# Functional programming is particularly helpful in this problem for several reasons:

# Immutability: The emphasis on immutability helps avoid unintended side effects and makes the code easier to reason about.

# Pure Functions: Pure functions simplify the understanding of the code and make it easier to test since they produce the same output for the same input without any hidden dependencies.

# List Comprehensions: Functional programming languages often provide concise and expressive features, such as list comprehensions, which are used in this solution to flatten the nested arrays.

# Readability: Functional programming tends to produce clear and declarative code, making it easier to understand the logic of the program.

# In summary, functional programming is a helpful paradigm for solving this problem because it encourages clear, concise, and expressive code while promoting immutability and the use of pure functions.


# Object Oriented Prompt
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


# Example usage:

# Create a generic Podracer
generic_podracer = Podracer(max_speed=300, condition="perfect", price=5000)

# Repair the generic Podracer
generic_podracer.repair()

# Create Anakin's Pod
anakins_pod = AnakinsPod(max_speed=400, condition="perfect", price=7000)

# Use the boost method for Anakin's Pod
anakins_pod.boost()

# Create Sebulba's Pod
sebulbas_pod = SebulbasPod(max_speed=350, condition="perfect", price=6000)

# Use the flame_jet method of Sebulba's Pod to trash another Podracer
sebulbas_pod.flame_jet(generic_podracer)

# Print the status of the Podracers
print("Generic Podracer:", generic_podracer.condition)
print("Anakin's Pod:", anakins_pod.max_speed, anakins_pod.condition)
print("Sebulba's Pod:", sebulbas_pod.condition)

# How does this solution demonstrate the four pillars of OOP?

# Encapsulation:

# The classes (Podracer, AnakinsPod, and SebulbasPod) encapsulate data (attributes like max_speed, condition, and price) and behavior (methods like repair, boost, and flame_jet) within themselves.
# Attributes are private to each class and accessed through methods, demonstrating encapsulation.
# Abstraction:

# Each class abstracts away the implementation details from the outside world. For example, the user of the AnakinsPod class doesn't need to know how the boost method works internally; they just need to know that calling it will increase the pod's speed.
# Inheritance:

# The classes AnakinsPod and SebulbasPod inherit from the base class Podracer.
# AnakinsPod and SebulbasPod reuse and extend the behavior of Podracer. It promotes code reuse and helps in organizing the code in a hierarchical manner.
# Polymorphism:

# Polymorphism is demonstrated in the example usage where instances of different classes (Podracer, AnakinsPod, and SebulbasPod) can be used interchangeably.
# For instance, the flame_jet method in SebulbasPod accepts any Podracer as an argument, showing polymorphic behavior.
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

# The choice of coding style depends on the specific requirements and preferences. For this problem, an object-oriented approach is suitable because:

# It models the problem naturally: Podracers have common attributes and behaviors but may have special characteristics (like boosting or flaming jets) that can be captured through inheritance.
# Object-oriented programming helps organize code hierarchically, making it more modular and extensible.
# A different coding style, such as a procedural or functional approach, might be possible, but it might not express the relationships between concepts as naturally as an object-oriented approach in this case.

# How did Object Oriented Programming assist in the solving of this problem?

# Modularity:

# The problem naturally involves different types of entities (Podracers, Anakin's Pod, Sebulba's Pod), making OOP a good fit for organizing code into modular, reusable units (classes).
# Hierarchy:

# Inheritance allows for a hierarchy of classes, reflecting the relationships between different types of Podracers.
# Readability:

# Object-oriented code tends to be more readable and understandable, especially when dealing with entities that have both data and behavior.
# Code Reusability:

# The solution leverages code reuse through inheritance. Common behavior is defined in the base class (Podracer), and specific behavior is added in the derived classes (AnakinsPod and SebulbasPod).