alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.(:)!?’[]{}%&*0123456789'
keys = [1, 2, 3, 5, 8]
text = 'I LOVE YOU'
ans = ''
for i, c in enumerate(text):
    text_index = alphas.find(c) + 1
    key = keys[i % len(keys)]
    print(c, text_index, key)
    ans += alphas[(text_index + key - 1) % len(alphas)]
print(ans)
