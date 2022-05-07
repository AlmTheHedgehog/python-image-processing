from PIL import Image

if __name__ == '__main__':
    im_yoda = Image.open("yoda.jpeg")
    yoda_arr = list(im_yoda.getdata())


    yoda_arr_gray = [[0]*3] * (im_yoda.height*im_yoda.width)
    number_of_pixels = [0] * (im_yoda.height*im_yoda.width)
    pdf = [0] * (im_yoda.height*im_yoda.width)
    cdf = [0] * (im_yoda.height*im_yoda.width)
    yoda_arr_eq_changes = [0] * (im_yoda.height*im_yoda.width)
    #to grayscale and count number of pixels per level
    for i in range(len(yoda_arr_gray)):
        yoda_arr_gray[i] = [int(yoda_arr[i][0]*0.299 + yoda_arr[i][1]*0.587 + yoda_arr[i][2]*0.114)] * 3
        number_of_pixels[yoda_arr_gray[i][0]] += 1

    #pdf and cdf calc + eq value 
    for i in range(len(yoda_arr_gray)):
        pdf[i] = number_of_pixels[i] / (im_yoda.height*im_yoda.width)
        if i == 0:
            cdf[i] = pdf[i]
        else:
            cdf[i] = cdf[i-1] + pdf[i]
        yoda_arr_eq_changes[i] = round(cdf[i] * 256)

    #changing input pixels values to eq
    for i in range(len(yoda_arr_gray)):
        yoda_arr_gray[i] = tuple([yoda_arr_eq_changes[yoda_arr_gray[i][0]]] * 3)


    im_yoda_eq = Image.new(im_yoda.mode, im_yoda.size)
    im_yoda_eq.putdata(yoda_arr_gray)
    im_yoda_eq.save("yoda_eq.jpg")