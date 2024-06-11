#Libraries
import pandas as pd

#Functions

def populairste_unisex_namen (df):
    
    '''Deze functie filtert de unisex namen uit een DataFrame en toont de populairste voor mannen, vrouwen en in het algemeen'''
        
    # Group by naam en tel voorkomen
    mannennamen_counts = df[df['geslacht'] == 'Mannelijk']['naam'].value_counts()
    vrouwennamen_counts = df[df['geslacht'] == 'Vrouwelijk']['naam'].value_counts()

    # Vind overlap
    unisex_names = mannennamen_counts.index.intersection(vrouwennamen_counts.index)

    # Vind populairste namen
    top_unisex_man = mannennamen_counts.loc[unisex_names].nlargest(1).index[0]
    top_unisex_vrouw = vrouwennamen_counts.loc[unisex_names].nlargest(1).index[0]
    top_unisex = pd.concat([mannennamen_counts, vrouwennamen_counts], axis=1, keys=['Mannelijk', 'Vrouwelijk']).sum(axis=1)
    top_unisex = top_unisex[top_unisex.index.isin(unisex_names)].nlargest(1).index[0]

    print(f"Populairste unisex naam bij de mannen: {top_unisex_man}")
    print(f"Populairste unisex naam bij de vrouwen: {top_unisex_vrouw}")
    print(f"Populairste unisex naam in het algemeen: {top_unisex}")