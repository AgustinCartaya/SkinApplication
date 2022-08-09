def run(images, info):
    print("Launching AI-03...")
    print("Given images:")
    for img_name, imgs in images.items():
        print("\t"+ img_name + ":")
        for img in imgs:
            print("\t\t" + img)
    print("Other information:")
    for info_name, infos in info.items(): 
        print("\t"+ info_name + ":")
        for info in infos:
            print("\t\t" + str(info))

    
    print("Calculating results...")

    results = {
        "risk":"malignat",
        "type":"melanoma",
        "Accurance":87
    }

    return results