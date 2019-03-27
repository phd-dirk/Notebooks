import json

mode = 'normal' # can be normal, sparse or weightCombinations

variables = {
    "astau": {
        "fixed": True,
        "value": 0.3317,
        "stepSize": 0.1
    },
    "aGGInv": {
        "fixed": True,
        "value": 2.1e-2,
        "stepSize": 0.01
    },
    "rhoVpA": {
        "fixed": False,
        "value": -0.5,
        "stepSize": 0.1
    },
    "c8VpA": {
        "fixed": False,
        "value": -0.5,
        "stepSize": 0.1
    },
    "c10": {
        "fixed": True,
        "value": -0.5,
        "stepSize": 0.1
    },
    "c12": {
        "fixed": True,
        "value": 0.020061955135371096,
        "stepSize": 0.1
    },
    "deltaV": {
        "fixed": True,
        "value": 3.56,
        "stepSize": 0.1
    },
    "gammaV": {
        "fixed": True,
        "value": 0.58,
        "stepSize": 0.1
    },
    "alphaV": {
        "fixed": True,
        "value": -1.92,
        "stepSize": 0.1
    },
    "betaV": {
        "fixed": True,
        "value": 4.07,
        "stepSize": 0.1
    },
    "deltaA": {
        "fixed": True,
        "value": 1.68,
        "stepSize": 0.1
    },
    "gammaA": {
        "fixed": True,
        "value": 1.41,
        "stepSize": 0.1
    },
    "alphaA": {
        "fixed": True,
        "value": 5.16,
        "stepSize": 0.1
    },
    "betaA": {
        "fixed": True,
        "value": 2.13,
        "stepSize": 0.1
    }
}


s0s = [
    3.1572314596000002, 3.000, 2.800, 2.600, 2.400, 2.300,
    2.200, 2.100, 2.000, 1.950, 1.900, 1.850,
    1.800, 1.750, 1.700, 1.675, 1.650, 1.625,
    1.600, 1.575, 1.550, 1.525, 1.500
    #,1.475,
    # 1.450, 1.425, 1.400, 1.375, 1.350, 1.325,
    # 1.300, 1.275, 1.250, 1.225, 1.200, 1.175,
    # 1.150, 1.125, 1.100, 1.075, 1.050, 1.025,
    # 1.000, 0.975, 0.950, 0.925, 0.900, 0.875,
    # 0.850, 0.825, 0.800, 0.775, 0.750, 0.725,
    # 0.700, 0.675, 0.650, 0.625, 0.600, 0.575,
    # 0.550, 0.525, 0.500, 0.475, 0.450, 0.425,
    # 0.400, 0.375, 0.350, 0.325, 0.300, 0.275,
    # 0.250, 0.225, 0.200, 0.175, 0.150, 0.125
]
dsbins = [
    0.075, 0.05, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025,
    0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025,
    0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025,
    0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025,
    0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025,
    0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.05,
    0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.175, 0.325
]

#s0s.sort()
weightDict = {1: 'wKin', 14: 'wCube', 15: 'wQuart'}
weight = 1

def dof(s0s, variables):
    dof = len(s0s)
    if not variables['astau']['fixed']:
        dof -= 1
    if not variables['aGGInv']['fixed']:
        dof -= 1
    if not variables['rhoVpA']['fixed']:
        dof -= 1
    if not variables['c8VpA']['fixed']:
        dof -= 1
    if not variables['c10']['fixed']:
        dof -= 1
    if not variables['c12']['fixed']:
        dof -= 1

    return dof


configTemplate = {
    "version": 0.9,
    "scheme": "FO",
    "tolerance": 1e-6,
    "parameters": {
        "asTau": 0.3156,
        "nc": 3,
        "nf": 3,
        "order": 5,
        "RVANormalization": 0.99743669,
        "mTau": 1.77686,
        "muMTau": 2.8e-3,
        "mdMTau": 5.0e-3,
        "msMTau": 97.0e-3,
        "be": 17.815,
        "dBe": 0.023,
        "vud": 0.97420,
        "dVud": 0.00021,
        "SEW": 1.0198,
        "dSEW": 0.0006,
        "mPiM": 0.13957018,
        "fPi": 92.21e-3,
        "dFPi": 0.14e-3,
        "f1P": 2.2e-3,
        "m1P": 1.3,
        "g1P": 0.4,
        "f2P": 0.19e-3,
        "m2P": 1.8,
        "g2P": 0.21,
        "input": [{
            "weight": weight,
            "s0s": s0s
        }]
    },
    "condensates": {
        "uuMTau": -0.020123648000000004,
        "ddMTau": -0.020123648000000004,
        "ssMTau": -0.016098918400000006
    },
    "thMomContribs": {
        "D0": True,
        "D2": False,
        "D4": True,
        "D6": True,
        "D8": True,
        "D10": False,
        "D12": False,
        "DV": False,
        "PionPole": True
    },
    "variables": variables
}


if mode == 'normal':
    i = 0
    for s0 in s0s:
        if dof(s0s[:i+1], variables) > 0:
            f = open("smin"+str(s0s[i]).replace(".","")+".json", "w")
            configTemplate["parameters"]["input"][0]["s0s"] = s0s[:i+1]
            f.write(json.dumps(configTemplate, indent=2))
        i += 1
elif mode == 'weightCombinations':
    weightCombinations = [[1, 14], [1, 15], [14, 15], [1, 14, 15]]
    s0sNum = 6
    for index, weights in enumerate(weightCombinations):
        xS0s = s0s[0:int(round(s0sNum / len(weights)))]
        usedWeightsStr = ''
        configTemplate['parameters']['input'] = []
        for wIdx, weight in enumerate(weights):
            configTemplate['parameters']['input'].append({
                's0s': xS0s,
                'weight': weight
            })
            usedWeightsStr += weightDict[weight]+'_'

        f = open(usedWeightsStr+"smin"+str(xS0s[-1]).replace(".","")+".json", "w+")
        f.write(json.dumps(configTemplate, indent=2))



elif mode == 'sparse':
    for i in range(1,9): # change range for different sparse settings
        s0sNum = 10
        xS0s = s0s[0::i][0:s0sNum]
        weights = [1, 14, 15]
        configTemplate["parameters"]["input"][0]["s0s"] = xS0s # get the first s0s from every ith bin
        for weight in weights:
            configTemplate["parameters"]["input"][0]["weight"] = weight
            f = open(weightDict[weight]+"_smin"+str(xS0s[-1]).replace(".","")+".json", "w+")
            f.write(json.dumps(configTemplate, indent=2))
