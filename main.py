from math_operations import addition
from package import package_2
from utils import greet
greet("Алексей")

import package

package.package_1()
package.package_2()

print(package.NAME)

import math_operations

math_operations.addition(4, 6)
math_operations.subtraction(4, 6)

print(math_operations.addition(4, 6))
print(math_operations.subtraction(4, 6))
print(math_operations.NAME)

