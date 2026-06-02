class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])

            elif op == 'D':
                record.append(record[-1] * 2)
                
            elif op == 'C':
                record.pop()
            
            else:
                record.append(int(op))

            
        return sum(record)

def is_int(x):
    try:
        num = int(x)
        return True
    except:
        return False
        