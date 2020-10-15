import re

def lulupet_uart_string_parser(string_to_parse):
    values = re.search('.*lulupet1234:\s*\[(.*?)\]', string_to_parse).group(1)

    return tuple(values.split(','))

if __name__ == '__main__':
    # string_to_parse為預計可以從termainal拿到的字串
    # parser會找出字串lulupet1234:後面[]中的值，並用,作切分
    string_to_parse = 'skdjhfalwkfelulupet1234:[1, 254.48]sdf,gbnalrg'
    pir, weight = lulupet_uart_string_parser(string_to_parse)
    
    print('pir: ' + pir)
    print('weight: ' + weight)