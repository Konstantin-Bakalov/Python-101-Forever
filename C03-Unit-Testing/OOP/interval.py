class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_inside(self, value):
        return self.start <= value <= self.end
    
    def stringify(self):
        start_symbol = '['
        end_symbol = ']'

        return f'{start_symbol}{self.start}, {self.end}{end_symbol}'
    
    def __str__(self):
        return self.stringify()
    
    def __repr__(self):
        return self.stringify()
    
interval = Interval(1, 10)
print(interval.stringify())
print(interval)
print(str(interval))
print(interval.is_inside(1))
print(interval.is_inside(5))
print(interval.is_inside(10))
print(interval.is_inside(12))