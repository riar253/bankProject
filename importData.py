import pandas as pd

with open(r'your directory path to dataset', 'r') as f:
    lines = f.readlines()
    data = [line.strip().split(';') for line in lines]

df = pd.DataFrame(data[1:], columns=data[0]).applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)

df.columns = [col.strip('"') for col in df.columns]

#####exploratory data analysis
#consider checking value types for each variable, and convert those that should be numeric to numeric
#check distributions of numerical variables - will inform whether we need to transform
#check countplot of categorical variables - would inform whether we need to downsize (might make model skewed)
#heatmap for numerical variables to show correlations
#chi_2 contingency using carmer's v heatmap for categorical variables to show correlations
