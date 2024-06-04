# Examen Data Scientist

Maia Francx De Gelder <br>
Juni 2024
<br>
<br>

Hierbij de instructies om de GitHub (LINK) te gebruiken.

## Te installeren

De .yaml-file staat rechtstreeks in de root-directory van dit project. <br>
<br>


## Titel

Voor dit deel moet slechts 1 Notebook <b>"naam.ipynb"</b> worden uitgevoerd. <br>
Die Notebook verwijst naar het <b>Tools.py</b> bestand (ondergebracht in Scripts) waarin imports, functies en constanten worden gedefinieerd en naar het <b>Styling.py</b> bestand.


### Data Analyse

- Een eerste visualisatie toont de productie over de voorbije jaren. <br>
Hierbij valt op dat de maximale productie (rode lijn) nooit wordt bereikt en dat er behoorlijk wat dagen met nul-productie zijn. <br>
Zoals aangegeven in de opgave, worden de dagen met <b>nul-productie wegens maintenance</b> uit de dataset <b>verwijderd</b>. <br>
<br>
- Het histogram voor de productie in <b>Brussel</b> toont een aanzienlijk aantal nul-dagen, <br>
met daarnaast een productie die normaalverdeeld lijkt en nauwelijks outliers kent. <br>
<br>
- Het histogram voor de productie in <b>Stockholm</b> toont minder nul-dagen, <br>
met daarnaast een productie die iets minder normaalverdeeld lijkt door de aanwezigheid van toch wel wat outliers. <br>


### Modeleren van 1 Productiedag

Het modelleren van een productiedag bestaat uit het bepalen van <br>
- enerzijds het percentage nul-dagen (18% voor BRU, 7% voor STO), en <br>
- anderzijds de parameters van de normaalverdeling die de niet-nul-dagen het best fit. <br>

Aangezien de niet-nul-producties meer normaalverdeeld zijn voor BRU dan voor STO, <br>
wordt er verwacht dat de "normaal-fitting" beter zal zijn voor BRU dan voor STO. <br>


### Simuleren van 1 Productiedag

Op basis van het model, wordt een BRU/STO dagproductie 2000 keer gesimuleerd. <br>
Daarna wordt het density histogram van de simulaties vergeleken met het densitiy histogram van de oorspronkelijke observaties. <br>
De overeenkomst is uitstekend voor BRU, en meer dan behoorlijk voor STO. <br>


### Simuleren van n Productiedagen

Een gesimuleerde productie voor een periode van n dagen is de <b>som</b> van n gesimuleerde dagproducties. <br>
Op basis van het model, wordt de BRU/STO productie voor een periode van n dagen 2000 keer gesimuleerd. <br>
De 2000 gesimuleerde BRU/STO producties voor een periode van n dagen worden gevisualiseerd in een histogram en in een empirische cumulatieve distributiefunctie (ecdf).

Met n = 7, merken we dat de BRU/STO weekproductie neigt naar een normale verdeling. <br>
De BRU weekproductie toont nog wat "gaten" die te wijten zijn aan de grote kans (18%) op nul-productie. <br>
<font color="blue"> Merk op dat je de waarde van n in de Notebook zelf kan wijzigen. <br>
    
Rode vertikale lijnen zijn toegevoegd aan de ecdf visualisaties. <br>
Die lijnen markeren de kans dat de productie voor een periode van n dagen respectievelijk lager ligt dan 25%, 50% en 75% van de theoretisch maximale productie voor een periode van n dagen.


### Centrale Limietstelling    

De Centrale Limietstelling zegt dat de <b>som_n</b> van een willekeurig variabele, hier de BRU/STO dagproductie, <br>
meer en meer normaalverdeeld wordt, naarmate n toeneemt. <br>
Die vaststelling was al zichtbaar in bovenstaande histogrammen en ecdf's voor n = 7. <br>
De laatste visualisatie verduidelijkt die toenemende normalisatie voor respectievelijk n = 2, 5, 10 en 20. <br>
<font color="blue"> Merk op dat je de waarden van n in de Notebook zelf kan wijzigen. <br>
<br>    


## Deel 2 : Verkoop tweedehands Volvo's

Voor dit deel moet slechts 1 Notebook <b>"autoproductie.ipynb"</b> worden uitgevoerd. <br>
Die Notebook bevat zowel de code om de data te manipuleren en te visualiseren, alsook de antwoorden op de vragen. <br>
<br>
    
    
    Introduction
This project involves analyzing a simulated dataset of births in Belgium for the year 2019. The data is contained in .csv files, each labeled with the actual birth date of the individuals in the file. The goal is to explore this dataset through various data manipulation and visualization techniques.

Here's a concise description of your project's folder structure and files:

examen_env.yml: YAML file specifying the conda environment for the project.
data/geboortes/: Directory containing CSV files with birth data for 2019.
examen.ipynb: Jupyter Notebook with the data analysis code and findings.
opgave.pdf: PDF document outlining the data science exam assignment.
README.md: Markdown file providing an overview and instructions for the project.
This structure organizes the environment setup, data, analysis, assignment details, and project documentation.

Key Steps:
Create a Virtual Environment and export a .yml file to include in the codebase.
Set up a GitHub page with a .gitignore and readme.md, and include a link to the GitHub repo in the readme file.
Clean up the code for clarity and understandability.
At the end, create a .zip file of the entire codebase for submission.
Code Breakdown
Step 1: Data Import
The first block of code involves iterating over all files in the data/geboortes directory, reading each .csv file, and merging them into one large DataFrame. An extra column is added to represent the "day of the year" for each birth date.

Getting to Know Our Data
This section converts 'verwachte datum' (expected birth date) to a datetime object and handles invalid dates in 'werkelijke datum' (actual birth date). It provides an overview of the dataset structure and types.

Step 2: Daily Birth Analysis
Question 1:
A plot is created to visualize the number of births per day throughout the year.

Question 2: Outlier Identification and Handling
Dates with birth counts deviating more than 50% from the average are classified as outliers and are addressed appropriately. Notably, outliers on January 1 and July 1 are due to misrecorded dates and are removed from the main dataset and added to df_wrong.

Step 3: Research Questions
Research 1: Unisex Names
Several questions regarding unisex names in the dataset are answered, including the number of unisex names, the most common unisex name among males and females, and the most popular unisex name overall.

Visualization:
A visualization is created to show all genuine unisex names and their relative occurrences among males and females.

Research 2: Accuracy of Estimated Delivery Dates
A comparison is made between the total number of births per day and the total number of expected births. A histogram and scatter plot are used to analyze the deviation from expected birth dates.

Research 3: Number of Names vs. Number of Babies
An investigation into the relationship between the number of unique names and the number of babies born. This section challenges the linear assumption of this relationship and encourages a deeper analysis based on the provided dataset.

Conclusion
Each code block serves a specific purpose in the data analysis process, from data preparation and cleaning to in-depth analysis and visualization. This readme provides a concise summary of each step, guiding the reader through the logical flow of the project.



