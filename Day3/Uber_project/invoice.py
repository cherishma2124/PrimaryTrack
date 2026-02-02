def getInvoice(**kwargs):
    ls=[]
    for key,value in kwargs.items():
        ls.append(f"{key} = {value}")
    return ls