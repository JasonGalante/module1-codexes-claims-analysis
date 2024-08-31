import pandas as pd

# import the csv file using pandas

data = pd.read_csv('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv' ,
                   sep='|')
# quick check of the data

data

# list the columns to identify codexes

for i in data.columns:
      print(i)

# find and print all codexes that start with "ICD"
# print the list
# count the number of ICD columns

icd_codes = [i for i in data if 
             i.startswith('ICD')]
print("ICD Codes:\n" ,data[icd_codes])
print("The number of ICD codes is:\n" 
      ,data.columns.str.startswith('ICD_').sum())

# find and print all codexes that start with "CLM"
# print the list
# count the number of CLM columns

clm_codes = [j for j in data if 
               j.startswith('CLM')]
print("CLM Codes:\n" ,data[clm_codes])
print("The number of claim codes is:\n" 
      ,data.columns.str.startswith('CLM_').sum())

# find and print all codexes that start with "HCPCS"
# print the list
# count the number of HCPCS columns

hcpcs_codes = [i for i in data if 
             i.startswith('HCPCS')]
print("HCPCS Codes:\n" ,data[hcpcs_codes])
print("The number of HCPCS codes is:\n" 
      ,data.columns.str.startswith('HCPCS_').sum())

# find and print all codexes that start with "DRG"
# print the list
# count the number of DRG columns

drg_codes = [i for i in data if 
             i.startswith('DRG')]
print("DRG Codes:\n" ,data[drg_codes])
print("The number of DRG codes is:\n" 
      ,data.columns.str.startswith('DRG_').sum())

missing_icd = data[icd_codes].isnull().sum()
missing_clm = data[clm_codes].isnull().sum()
missing_hcpcs = data[hcpcs_codes].isnull().sum()
missing_drg = data[drg_codes].isnull().sum()

print(f"Missing ICD Codes:\n {missing_icd}")
print(f"Missing ICD Codes:\n {missing_clm}")
print(f"Missing ICD Codes:\n {missing_hcpcs}")
print(f"Missing ICD Codes:\n {missing_drg}")


