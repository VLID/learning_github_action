content='Hello Github Actions'

with open('new_file.txt','w') as f:
    f.write(content)

print(content)
