def run(images, info):
    print("Launching AI-01...")
    print("Given images:")
    for img_name, imgs in images.items():
        print("\t"+ img_name + ":")
        for img in imgs:
            print("\t\t" + img)
    print("Other information:")
    for info_name, infos in info.items(): 
        print("\t"+ info_name + ":")
        for i_name, i_value in infos.items():
            print("\t\t" + i_name + ": " + str(i_value))

    #Calculate results

    results = {
        "risk":"malignant",
        "type":"melanoma",
        "Accurance":87
    }
    return results