print ('Enter arrow base height: ')
arrow_base_height = int(input())

print ('Enter arrow base width: ')
arrow_base_width = int(input())

print ('Enter arrow head width: ')
arrow_head_width = int(input())

while arrow_head_width <= arrow_base_width:
    print ('Enter arrow head width: ')
    arrow_head_width = int(input())

for i in range(arrow_base_height):
    print('*' * arrow_base_width)
else:
    for j in reversed(range(arrow_head_width + 1)):
        print('*' * j)
        if j == 1:
            break
