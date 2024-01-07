import random
import string

def random_user_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))

# Test the function
print(random_user_id())

def user_id_gen_by_user():
    num_characters = int(input("123456789: "))
    num_ids = int(input("6: "))
    
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_characters))
        user_ids.append(user_id)
    
    return user_ids

# Test the function
print(user_id_gen_by_user())  # Example 1
print(user_id_gen_by_user())  # Example 2

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

# Test the function
print(rgb_color_gen())

def list_of_hexa_colors(num_colors):
    return ['#' + ''.join(random.choice('0123456789abcdef') for _ in range(6)) for _ in range(num_colors)]

# Test the function
print(list_of_hexa_colors(3))
print(list_of_hexa_colors(1))

def list_of_rgb_colors(num_colors):
    return [f'rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})' for _ in range(num_colors)]

# Test the function
print(list_of_rgb_colors(3))
print(list_of_rgb_colors(1))

def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return []

# Test the function
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
