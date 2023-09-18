def remove_duplicates(sequence):
    unique_elements = []
    
    for item in sequence:
        if item not in unique_elements:
            unique_elements.append(item)
    
    return unique_elements

