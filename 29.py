def data_reverse(data):
    var = ''
    data = str(data)
    data = data.replace(',', '')
    # for i in range(0, len(data)+1, 8):
    #     if i == '':
    #         data.remove(i)
    #     if i > 0:
    #         var.append(data[:i])
    #     elif i > 8:
    #         var.append(data[i-8:i])
    # print(var)


data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0])
