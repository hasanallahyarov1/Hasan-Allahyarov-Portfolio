def document_type(file):
    x=file[:1000]
    if  "10-K" in x:
        y="10-K"
    elif "10-Q" in x:
        y="10-Q"
        
    return y
