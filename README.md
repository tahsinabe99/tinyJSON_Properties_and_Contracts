# Properties and Contracts for tinyJSON

Algorithm for  properties and contracts for a program called tinyJSON using hypothesis and icontract, property-based testing frameworks.
The goal is to verify the provided properties and contracts achieve a specific statement coverage threshold when tested.

Properties: These are statements or assertions about the expected behaviour of the code that should hold true for any input. Properties are more general than individual test cases.
Example: If we have a function add(x, y) that adds two numbers, a property might state that add(x, y) should always equal add(y, x).

Contracts: These are explicit conditions (preconditions, postconditions and invariants) that must be true before or after the execution of a function.
Example: For the same add(x, y) function, a postcondition might state that the result should always be greater than or equal to either x or y.
