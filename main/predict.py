from model import load_model

def predict():
    file = input('Name of image to be classfied(file[0 - 12]), or own file:\n')
    try:
        a = int(file)
        file = 'file' + str(a)
        label, confidence = load_model(file)
    except:
        label, confidence = load_model(file)

    categories = []
    with open('../data/words.txt', 'r') as r:
        for line in r:
            a = line.split()
            categories.append(a[1 : ])
    return categories[int(label)], confidence
if __name__ == '__main__':
    label, confidence = predict()
    print('Label: {}\nConfidence: {}'.format(label, confidence))
