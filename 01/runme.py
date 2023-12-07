inputfiles = ['example1.txt','example2.txt','input.txt']

for filename in inputfiles:
    with open(filename) as file:
        calibrations = file.read().splitlines()

    inputs = []
    translations = ['','one','two','three','four','five','six','seven','eight','nine']
    for entry in calibrations:
        first = False
        word = ''
        for i,c in enumerate(entry):
            d = c
            if entry[i:i+3] in translations:
                d = str(translations.index(entry[i:i+3]))
            elif entry[i:i+4] in translations:
                d = str(translations.index(entry[i:i+4]))
            elif entry[i:i+5] in translations:
                d = str(translations.index(entry[i:i+5]))
            if (not first) and d.isdigit():
                first = True
                x1 = int(d)*10
            if d.isdigit():
                x2 = int(d)
        inputs.append(x1+x2)

    print(sum(inputs))