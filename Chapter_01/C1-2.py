# Asks for the radius of a sphere and returns the volume.

def get_sphere_volume(r: int) -> int:
    volume = (4 / 3 * 3.14159 * r ** 3)
    return volume


if __name__ == '__main__':
    radius = int(input("What is the radius of your sphere? "))
    volume = get_sphere_volume(radius)
    print(f"The volume of your sphere is {volume:.3f}.")
