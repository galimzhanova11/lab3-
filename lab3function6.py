 
def reverse_word(sent, start, end):
    while start < end:
        sent[start], sent[end] = sent[end], sent[start]
        start = start + 1
        end -= 1
 
 
sent = input()
sent = list(sent)
start = 0
while True:
    try:
        end = sent.index(' ', start)
        reverse_word(sent, start, end - 1)
        start = end + 1
    except ValueError:
        reverse_word(sent, start, len(sent) - 1)
        break
    
sent.reverse()
sent = "".join(sent)
 
print(sent)