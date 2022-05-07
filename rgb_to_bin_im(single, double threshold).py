from PIL import Image

if __name__ == '__main__':
    im_yoda = Image.open("yoda.jpeg")
    yoda_arr = list(im_yoda.getdata())

    answ = "3"
    while (answ != "1") and (answ != "2"):
        answ = input("Single TH - 1; double - 2:")
        if answ == "1":
            is_singleTH = True
        elif answ == "2":
            is_singleTH = False
        else:
            print("Eroor, try one more")

    answ = 256
    while not (0 <= answ <= 255):
        answ = int(input("Enter first threshold(0 <= answer <= 255):"))
    threshold = [answ]
    if not is_singleTH:
        answ = 256
        while not (0 <= answ <= 255):
            answ = int(input("Enter second threshold(0 <= answer <= 255):"))
        threshold.append(answ)

    #to grayscale and binary
    yoda_arr_bin = [[0]*3] * (im_yoda.height*im_yoda.width)
    for i in range(len(yoda_arr_bin)):
        if (yoda_arr[i][0]*0.299 + yoda_arr[i][1]*0.587 + yoda_arr[i][2]*0.114) >= threshold[0]:
            if not is_singleTH:
                if (yoda_arr[i][0]*0.299 + yoda_arr[i][1]*0.587 + yoda_arr[i][2]*0.114) <= threshold[1]:
                    yoda_arr_bin[i] = tuple([255, 255, 255])
                else:
                    yoda_arr_bin[i] = tuple([0, 0, 0])
            else:
                yoda_arr_bin[i] = tuple([255, 255, 255])
        else:
            yoda_arr_bin[i] = tuple([0, 0, 0])

    im_yoda_binary = Image.new(im_yoda.mode, im_yoda.size)
    im_yoda_binary.putdata(yoda_arr_bin)
    im_yoda_binary.save("yoda_binary.jpg")