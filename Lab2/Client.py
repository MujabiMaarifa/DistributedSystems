import Pyro4
# Connect to the server using the URI
greeting_uri = "PYRONAME:Greeting"
calculator_uri = "PYRONAME:Calculations"
student_uri = "PYRONAME:Student"

#access the exposed objects
try:
    greeting = Pyro4.Proxy(greeting_uri)
    calculator = Pyro4.Proxy(calculator_uri)
    student = Pyro4.Proxy(student_uri)

    # Call remote method
    print(greeting.say_hello("Alice"))
    print()
    print("Addition: ", calculator.add(4,5))
    print("Subtraction: ", calculator.subtract(10,8))
    print("Division by non zero: ", calculator.divide(10,3))
    print("Division by zero: ", calculator.divide(10,0))
    print(student.getStudent("Arnold Mutwiri", "C026-01-0802/2024"))
except ServerException:
    print("Could not connect to the exposed proxy")


