import Pyro4
import time
# Connect to the server using the URI
greeting_uri = "PYRONAME:Greeting"
calculator_uri = "PYRONAME:Calculations"
student_uri = "PYRONAME:Student"
service_uri = "PYRONAME:report.service"
counter_uri = "PYRONAME:counter"
auth_uri = "PYRONAME:Auth"

#access the exposed objects
try:
    auth = Pyro4.Proxy(auth_uri)
    greeting = Pyro4.Proxy(greeting_uri)
    calculator = Pyro4.Proxy(calculator_uri)
    student = Pyro4.Proxy(student_uri)
    service= Pyro4.Proxy(service_uri)
    future = Pyro4.Future(service.generateReport)
    counter = Pyro4.Proxy(counter_uri)

    auth._pyroHmacKey = b"12345"
    try:
        result = auth.getSecretData()
        print(result)
    except Exception as e:
        print("Access Denied:", e)

    for i in range(15):
        counter.increment()
    print("Current count: ", counter.getCount())

    print("Request sent...")

    future()


    # Continue doing other work
    print("Performing other work...")

    for i in range(5):
        print("Working...", i)
        time.sleep(1)

    # Call remote method
    print(greeting.say_hello("Alice"))
    print()
    print("Addition: ", calculator.add(4,5))
    print("Subtraction: ", calculator.subtract(10,8))
    print("Division by non zero: ", calculator.divide(10,3))
    print("Division by zero: ", calculator.divide(10,0))
    print(student.getStudent("Arnold Mutwiri", "C026-01-0802/2024"))

    print("Client finished")
except Exception as e:
    print("Method could not be found! ", e)


