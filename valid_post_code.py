import re

P = input()
regex_integer_in_range = r"^[1-9]([\d]){4}([1-9])$"	
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)  # La expresion alternating digit pair entrega solamente un match o un patter de busqueda, es por eso que el re.findall se le coloca len para que solamente entregue lo que sea menor que 2.
