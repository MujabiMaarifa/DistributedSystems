import Pyro4
import json
import time
import os

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


STATE_FILE = "counter_state.json"


@Pyro4.expose
class CounterService:

    def __init__(self):
        self.count = 0
        self.load_state()

    def increment(self):
        self.count += 1
        self.save_state()
        return self.count

    def getCount(self):
        return self.count


    def save_state(self):
        with open(STATE_FILE, "w") as f:
            json.dump({"count": self.count}, f)
    def load_state(self):
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    data = json.load(f)
                    self.count = data.get("count", 0)

            except json.JSONDecodeError:
                # file exists but has no valid JSON
                self.count = 0
                self.save_state()

            else:
                self.count = 0
                self.save_state()


# Setup the daemon and the name server
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

#instantiate counter
counter = CounterService()

# Register the objects
greeting_uri = daemon.register(Greeting)
calculator_uri = daemon.register(CalculatorService)
student_uri = daemon.register(StudentService)
report_uri = daemon.register(GenerateReport)
counter_uri = daemon.register(counter)

ns.register("Greeting", greeting_uri)
ns.register("Calculations", calculator_uri)
ns.register("Student", student_uri)
ns.register("report.service", report_uri)
ns.register("counter", counter_uri)

print("Server is ready...")
print("Report Service ready!")
print("Counter service is running!")
daemon.requestLoop()
