import pandas as pd

class SplitDateOnColumn:
    def fit(self, dataFrame):
        pass
    def transform(self, dataFrame):
        resDataDictColls = {"sku": [], "unit": [], "month": [], "resultValue": []}
        
        for serialId in range(0, len(dataFrame)):
            serial = dataFrame.values[serialId]
            for i in range(2, len(dataFrame.columns)):
                resDataDictColls["sku"] += [serial[0]]
                resDataDictColls["unit"] += [serial[1]]
                resDataDictColls["month"] += [dataFrame.columns[i]]
                resDataDictColls["resultValue"] += [serial[i]]
        result = pd.DataFrame(resDataDictColls)
        return result
    def fit_transform(self, dataFrame):
        return self.transform(dataFrame)
    
class SplitDateOnYearsMonth:
    def fit(self, dataFrame):
        pass
    def transform(self, dataFrame):
        dateData = dataFrame.loc[..., "month"]
        resDict = {"years": [], "month" : []}
        for dates in dateData:
            splittedText = dates.split("-")
            resDict["years"] += [int(splittedText[0])]
            resDict["month"] += [int(splittedText[1])]
        df = pd.DataFrame(resDict)
        df = dataFrame.drop("month", axis=1).join(df)
        return df
    def fit_transform(self, dataFrame):
        return self.transform(dataFrame)