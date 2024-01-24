class Kitty_kat:

    def __init__(self, armlength = 6.2, leglength = 6.5, eyes = 2, tail = True, furry = True):
        self.kitty_kat = {
            'armlength': armlength,
            'leglength': leglength,
            'eyes': eyes,
            'tail': tail,
            'furry': furry
        }

    def set_armlength(self, armlength):
        self.kitty_kat['armlength'] = armlength 

    def set_leglength(self, leglength):
        self.kitty_kat['type'] = leglength 

    def set_eyes(self, eyes):
        self.kitty_kat['eyes'] = eyes 

    def set_tail(self, tail):
        self.kitty_kat['type'] = tail

    def set_furry(self, furry):
        self.kitty_kat['type'] = furry

    def get_armlength(self):
        return self.kitty_kat['armlength']

    def get_leglength(self):
        return self.kitty_kat['leglength']
    
    def get_eyes(self):
        return self.kitty_kat['eyes']

    def get_tail(self):
        return self.kitty_kat['tail']

    def get_furry(self):
        return self.kitty_kat['furry']

    # Method for getting all kitty_kat info at once
    def __iter__(self):
        return iter(self.kitty_kat.items())

# Set class instance and set values
kitty_kat = Kitty_kat()
kitty_kat.set_armlength('6.2')
kitty_kat.set_leglength('6.4')
kitty_kat.set_eyes(2)
kitty_kat.set_tail(True)
kitty_kat.set_furry(True)

print(f'kitty_kat armlength: {kitty_kat.get_armlength()}')
print(f'kitty_kat leglength: {kitty_kat.get_leglength()}')
print(f'kitty_kat eyes: {kitty_kat.get_eyes()}')
print(f'kitty_kat tail: {kitty_kat.get_tail()}')
print(f'kitty_kat fur: {kitty_kat.get_furry()}')
 