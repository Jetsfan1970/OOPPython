"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """ Makes a new generator, with initialzed start value"""
        
        self.start = self.next = start
        
    def __repr__(self):
        """Shows the generator start and next number"""
        
        return f"<Serial Generator start={self.start} next={self.next}>"
        
    
    def generate(self):
        """Returns the starts number and then add 1 each time generate is run"""
        
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """ Resets number back to oringal value"""
        
        self.next = self.start
    
        
        
    
    
        

