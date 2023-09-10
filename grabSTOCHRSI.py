def get_StochasticRelitiveStrengthIndex(data, window, smooth1, smooth2):
    stochRSIind = StochRSIIndicator(data['close'], window, smooth1, smooth2)
    return stochRSIind.stochrsi_k() * 100, stochRSIind.stochrsi_d() * 100


if __name__ == '__main__':
    f = open("documents/data.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data) # turns data into pandas dataset
    stochRSIK, stochRSID = get_StochasticRelitiveStrengthIndex(data, 14, 3, 3)
    print(stochRSIK, stochRSID)
