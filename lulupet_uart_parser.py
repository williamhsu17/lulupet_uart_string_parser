import re

def lulupet_uart_string_parser(string_to_parse):
    values = re.search('.*lulupet1234:\s*\[(.*?)\]', string_to_parse).group(1)

    return tuple(values.split(','))

if __name__ == '__main__':
    string_to_parse = 'lulupet1234:[1, 254.48]'
    pir, weight = lulupet_uart_string_parser(string_to_parse)
    
    print('pir: ' + pir)
    print('weight: ' + weight)