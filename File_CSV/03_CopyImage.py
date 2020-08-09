with open("image1.jpg", "rb") as rf:
    with open("image1copy.jpg", "wb") as wf:
        for i in rf:
            wf.write(i)
