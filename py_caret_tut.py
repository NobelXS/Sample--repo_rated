import pandas as pd
from pycaret.classification import *

df = pd.read_csv('CaseStudyData.csv')
# print(df.head(10))

s = setup(df, target='TargetVariable')

best = compare_models()

print(best)

finalize_model(best)
evaluate_model(best)
predict_model(best)
save_model('lr', 'lr_model_v1')
