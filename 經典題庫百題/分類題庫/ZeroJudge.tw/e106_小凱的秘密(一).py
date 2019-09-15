alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.(:)!?’[]{}%&*0123456789'
key = 7
text = 'I LOVE YOU'
ans = ''
for i, c in enumerate(text):
    text_index = alphas.find(c) + 1
    print(c, text_index, key)
    ans += alphas[(text_index + key - 1) % len(alphas)]
print(ans)
