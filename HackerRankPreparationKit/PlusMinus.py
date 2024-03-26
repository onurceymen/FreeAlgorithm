def calculaRatios(arr):
    count = len(arr)
    positives = len([x for x in arr if x > 0])
    negatives = len([x for x in arr if x < 0])
    zeros = len([x for x in arr if x == 0])

    positive_ratio = positives / count
    negative_ratio = negatives / count
    zero_ratio = zeros / count

    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

array = [1, -2, 0, -4, 5]
calculaRatios(array)
