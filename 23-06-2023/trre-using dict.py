families = {
    'ram':
          {'raju':{'rahul','rohith'},
           'ramana':{'ramesh'}},
    'yashoda':
          {'yesh':{'yashoder'},
           'yegneshwar':{'yogeswar'},
           'yogi':{'yoginath'}},
    'charan':
          {'cherry':'charmi' , 'charani':'chawla'}
    }
for parent,children in families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(f" {',and '.join([str(child) for child in [*children]])}")
    
