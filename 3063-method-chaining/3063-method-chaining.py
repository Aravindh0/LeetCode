import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter for animals with weight greater than 100
    heavy_animals = animals[animals['weight'] > 100]
    
    # Sort the filtered DataFrame by the 'name' column in descending order
    heavy_animals_sorted = heavy_animals.sort_values(by='weight', ascending=False)
    
    # Return the resulting DataFrame containing only the 'name' column
    return heavy_animals_sorted[['name']].reset_index(drop=True)