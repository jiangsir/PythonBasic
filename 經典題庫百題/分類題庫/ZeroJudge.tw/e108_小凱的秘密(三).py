alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.(:)!?’[]{}%&*0123456789'
keys = 'PIG'
text = 'I LOVE YOU'
ans = ''
for i, c in enumerate(text):
    text_index = alphas.find(c) +1
    key_char = keys[i % len(keys)]
    key_index = alphas.find(key_char) +1
    print(c, text_index, key_char, key_index)
    ans += alphas[(text_index + key_index -1) % len(alphas)]
print(ans)
