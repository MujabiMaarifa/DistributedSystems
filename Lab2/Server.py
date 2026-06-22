import Pyro4
import time

@Pyro4.expose
class Greeting:
    def say_hello(self, name):
        return f"Hello, {name}!"

@Pyro4.expose
class CalculatorService:
    def add(self, a, b):
        print("add function running")
        return a+b
    def subtract(self, a, b):
        print("subtract function executing")
        return a-b
    def divide(self,a,b):
        print("Division function executing")
        try:
            result=a/b
            return result
        except ZeroDivisionError:
            return "Cannot Divide by Zero"

@Pyro4.expose
class StudentService:
    def getStudent(self, name, regNO):
        print("getStudent funtion running")
        return f"Student name: {name}, REG: {regNO}"

@Pyro4.expose
class GenerateReport:
    def generateReport(self):
        print("Generating Report...")
        time.sleep(10)
        return "Report generated successfully"


# Setup the daemon and the name server
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

# Register the objects
greeting_uri = daemon.register(Greeting)
calculator_uri = daemon.register(CalculatorService)
student_uri = daemon.register(StudentService)
report_uri = daemon.register(GenerateReport)

ns.register("Greeting", greeting_uri)
ns.register("Calculations", calculator_uri)
ns.register("Student", student_uri)
ns.register("report.service", report_uri)


print("Server is ready...")
print("Report Service ready!")
daemon.requestLoop()
