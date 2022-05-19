class TestResult:
    def __init__(self, warn, err):
        self.__warn = warn
        self.__error = err
    def __add__(self,second_op):
        return TestResult(self.__warn + second_op.__warn, self.__error + second_op.__error)
    def __str__(self):
        return f"Error = {self.__error}, Warnings = {self.__warn}"
    def __repr__(self):
        return f"TestResult({self.__warn},{self.__error})"        
        
x = TestResult(2,4)
y = TestResult(1,2)
o = x + y
print(o)
result_today = ((1,2),(3,4),(5,6))
result_yesterday = ((3,5),(10,12),(1,1))

test_results_today = [TestResult(i,j) for i,j in result_today]
test_results_yesterday = [TestResult(i,j) for i,j in result_yesterday]

print(test_results_today)
print(test_results_yesterday)

total_result = [ i + j for i,j in zip(test_results_today,test_results_yesterday) ]

print(total_result)