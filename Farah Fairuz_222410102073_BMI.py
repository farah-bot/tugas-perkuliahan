print('''
=========================================================================================================================
|                                                                                                                       |
|                                                     BMI CALCULATOR                                                    |
|                                                                                                                       |
=========================================================================================================================
''')

def weight():
    w = input("Enter your weight (kg) : ")
    global wf
    if isfloat_w(w) == True:
        wf = w
        wf = float(wf)
        height()
    elif w.isnumeric():
        wf = w
        wf = float(wf)
        height()
    else:
        print("Your input is not valid. Please try again.")
        return weight()

def isfloat_w(w):
    try:
        float(w)
        return True
    except ValueError:
        return False

def height():
    h = input("Enter your height (cm) : ")
    global hf
    if isfloat_h(h) == True:
        hf = h
        hf = float(hf)
        hf = hf/100
        bmi()
    elif h.isnumeric():
        hf = h
        hf = float(hf)
        hf = hf/100
        bmi()
    else:
        print("Your input is not valid. Please try again.")
        return height()

def isfloat_h(h):
    try:
        float(h)
        return True
    except ValueError:
        return False

def bmi():
    bmi_result = wf/(hf**2)
    print("\nYour body mass index (bmi) is {0} and your weight is defined as ".format(bmi_result), end="")

    if bmi_result >= 40:
        print("obesity class III\nReduce calories in your diet or burn your calories with exercise\n")
    elif 35 <= bmi_result < 39.9:
        print("obesity class II\nReduce calories in your diet or burn your calories with exercise\n")
    elif 30 <= bmi_result < 34.9:
        print("obesity class I\nReduce calories in your diet or burn your calories with exercise\n")
    elif 25 <= bmi_result < 29.9:
        print("overweight\nReduce calories in your diet or burn your calories with exercise\n")
    elif 18.5 <= bmi_result < 24.9:
        print("normal weight\nYou're in a great shape. Maintain it with regular exercise and a healthy diet\n")
    elif bmi_result < 18.5 :
        print("underweight\nGain your weight\n")


weight()
