from querypackage import functions

# Test get_query() function 
sql = '''select * from synthea_native.observations limit 10'''
print('''
==============================================
Testing get_query() function with input 
"{sql}"
==============================================
'''.format(sql=sql))
df = functions.get_query(sql)
print(df)


# Test get_person() function 
patient_list = ['cac10d78-b13d-660e-57ae-4ee7a6c84fc8']
print('''
==============================================
Testing get_person() function with input 
{patient_list}
==============================================
'''.format(patient_list=patient_list))
patient_df = functions.get_person(patient_list)
print(patient_df)