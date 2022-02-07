def input_file_read(a):    
    fh1 = open(a,'r')
    lines = fh1.readlines()
    fh1.close()
    return lines

def output_file_write(string_lines,b):    
    fh2 = open(b,'w')
    for lines in string_lines:
        fh2.write(lines)
    fh2.close()
    return string_lines

def upper_case_output(upper_case):
    output_upcase =[]
    for uppercase in upper_case:
        up_output = uppercase.upper()
        output_upcase.append(up_output)
    return output_upcase

input_file = "input_123.txt"
output_file = "output_123.txt"

lines_1 = input_file_read(input_file)
lines_2 = upper_case_output(lines_1)
result = output_file_write(lines_2,output_file)
print("hello all",result)
