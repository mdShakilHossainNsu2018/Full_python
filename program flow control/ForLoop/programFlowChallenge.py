ip = input("Enter the ip address: ")

if (len(ip) != 0) and (ip[-1] != '.'):
    ip += '.'

segment = 1
segment_len = 0
# dot = ''

for dot in ip:
    if dot == ".":
        print("segment {0} contain {1} characters".format(segment, segment_len))
        segment_len = 0
        segment += 1
    else:
        segment_len += 1

#
# if dot != '.':
#     print("segment {0} contain {1} characters".format(segment, segment_len))
























