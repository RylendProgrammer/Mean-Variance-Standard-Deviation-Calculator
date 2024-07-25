import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("Input must be a list of 9 digits")
    
    list_to_matrix = np.array(list).reshape(3, 3)

    mean = [(list_to_matrix.mean(axis=0).tolist()), (list_to_matrix.mean(axis=1).tolist()), (list_to_matrix.flatten().mean())]
    variance = [(list_to_matrix.var(axis=0).tolist()), (list_to_matrix.var(axis=1).tolist()), (list_to_matrix.flatten().var())]
    std_deviation = [(list_to_matrix.std(axis=0).tolist()), (list_to_matrix.std(axis=1).tolist()), (list_to_matrix.flatten().std())]
    maximum = [(list_to_matrix.max(axis=0).tolist()), (list_to_matrix.max(axis=1).tolist()), (list_to_matrix.flatten().max())]
    minimum = [(list_to_matrix.min(axis=0).tolist()), (list_to_matrix.min(axis=1).tolist()), (list_to_matrix.flatten().min())]
    summation = [(list_to_matrix.sum(axis=0).tolist()), (list_to_matrix.sum(axis=1).tolist()), (list_to_matrix.flatten().sum())]

    return_dict = { 
        'mean': mean,
        'variance': variance,
        'standard deviation': std_deviation,
        'max': maximum,
        'min': minimum, 
        'sum': summation
    }

    #return calculations
    return return_dict

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(calculate(my_list))