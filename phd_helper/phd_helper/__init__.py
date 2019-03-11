def getUncertaintyParenthesis(val, err):
    digits = 2

    eVal = '%e' % err
    errZeroes = int(eVal.partition('-')[2])-1
    parenthesisErr = int(round(err*10**(errZeroes+digits),0))
    return '{val:.0{width}f}'.format(val=val,width=errZeroes+digits)+'('+str(parenthesisErr)+')'

def dfToLatex(df,cols):
    table = ''
    for index, row in df.iterrows():
        firstCol = True
        for col in cols:
            if not firstCol:
                table += ' & '

            table += getUncertaintyParenthesis(row[col], row[col+'Err'])
            firstCol = False
        table += ' & '+str(round(row['chiDof'],2))+' \\\\\n'
    return table
