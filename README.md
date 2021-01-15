<!-- <div align="center">
    <div>
        <img src="uem_logo.jpg" style="width: 32%; padding: 2px;"><br>
        <img src="clab_logo.png" style="width: 32%; padding: 2px;">
    </div>
    <img src="oulu_logo.jpg" style="width: 20%; height: 200px; padding: 2px;">
</div> -->
# JBI14071
📑 <u>Article</u>: Little evidence of range size conservatism in freshwater plants across two continents
📔 <u>Journal</u>: Journal of Biogeography
🔗 [DOI](10.1111/jbi.14071)

This repository contain all the code and data for the reproducibility of the results obtained.



# Data 📂

The original data is in the `raw_data` folder. It consists of `shape files` for the aquatic plants in Europe and North America. We explore this data to produce called preprocessed data, creating grids of 50km², 100km², and 200km² within the continents. Each file is an adjacency matrix where each entry inform if a species occupies that grid within the continent. These files are in the folder `results`.

# Code 📝

All code was written in `python`. The notebooks found in the `first_analysis` folder contain the code used for exploratory analysis (`data_exploring.ipynb`) and results concerning the overlapping of sister species regions (`data_analysis.ipynb`) as well as environmental analysis (`env_feat_analysis.ipynb`). 

Due to a first revision, we had to clean some of our data. Therefore, all the code needed to reproduce the final results of the paper are in the folder `referee_response`. 

The code to reproduce the results of the null model is written in the file `null_model.py`, which can be run from a terminal specifying the parameters, in the following order: 
```python
n - int: number of species
N - int: number of links to create, i.e., 
         the number of pairs overlapping.
```

Code to calculate the patristic distance among species was written in R by Jorge and all files necessary to reproduce the results are in the folder `patristic_analysis_R`.

# Figures 📈

The disposition of panels in some of the final figures is different from those found within the `jupyter notebooks`. This is because their disposition within the figure was edited with the free software `inkscape` on the request upon the acceptance of the paper. We emphasize that only the disposition of the panels were made, not involving manipulation of any that whatsoever. The figures used in the paper are in the folder `figures`. 

# Authorship 🙋‍♂️

All `python` code and notebooks were written by me, `Vieira D. S.` The code in `R` was written by `Girón, J. G.`