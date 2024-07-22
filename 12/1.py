data = '8' * 68 
while '222' in data or '888' in data: 
    if '222' in data: 
        data = data.replace('222', '8', 1)
    else: 
        data = data.replace('888', '2', 1)
    
print(data)
