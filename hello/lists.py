basket = ['Apple', 'bun', 'Cola']
crate = ['Egg' , 'Fig' , 'Grape']
print( 'Basket List:')
print('Basket Elements:' ,len(basket))
basket.append('Damson')
print('Appended:',basket)
print('Last Item Removed:' , basket.pop())
print('Basket list:', basket)

basket.extend( crate)
print('Extended:', basket)
del basket[1]
print('item Removed:', basket)
del basket[1:3]
print('Slice Removed:', basket)