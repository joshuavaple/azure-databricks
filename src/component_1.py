from lib.utils import CONSTANT, add_two_integers


print(CONSTANT)
print(add_two_integers(1, 2))

if __name__ == "__main__":
    component_result = CONSTANT*add_two_integers(1, 2)
    print(component_result)