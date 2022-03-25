from gpio import Gpio

g = Gpio(0,False)
g.print_gpio()
print(g.get_state())
g.set_state(True)
g.print_gpio()
print(g.get_state())