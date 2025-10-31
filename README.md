# OTT-Hypothesis-Testing-An-Analytical-Study-of-Age-Restriction-and-Ratings-on-Netflix-vs-Disney

This repository contains a **data analysis project** that explores movies available on various streaming platforms. The analysis focuses on two main aspects of movies:

1. **Age Ratings** – Understanding the distribution of movie ages and how age relates to other factors.  
2. **Overall Ratings** – Understanding the distribution of movie ratings and analyzing trends.

The project includes data cleaning, visualization, and statistical hypothesis testing to extract meaningful insights.



## 📁 Folder Structure
```
C:.
├── data
│   ├── processed
│   │   ├── age_analysis.csv
│   │   └── rating_analysis.csv
│   └── raw
│       ├── movies_on_streaming_platforms.csv
│       └── sample_data.csv
├── outputs
│   └── figures
│       ├── age_graph.png
│       ├── age_scatter_plot.png
│       ├── rating_graph.png
│       └── rating_scatter_plot.png
├── src
│   ├── age_box_chart_analysis.py
│   ├── age_hypothesis_testing.py
│   ├── age_scatter_plot_analysis.py
│   ├── rating_box_chart_analysis.py
│   ├── rating_hypothesis_testing.py
│   └── rating_scatter_plot_analysis.py
├── LICENSE
├── README.md
└── requirements.txt

```




## 📂 Description of Folders and Files

- **`data/raw`**  
  Contains the original datasets:  
  - `movies_on_streaming_platforms.csv` – Main dataset with movie information across streaming platforms.  
  - `sample_data.csv` – Sample dataset for testing and experimenting.

- **`data/processed`**  
  Contains cleaned and processed datasets ready for analysis:  
  - `age_analysis.csv` – Prepared data for age-related analysis.  
  - `rating_analysis.csv` – Prepared data for rating-related analysis.

- **`outputs/figures`**  
  Stores visualizations generated from the analysis scripts:  
  - Box plots and scatter plots for both age and ratings.

- **`src`**  
  Contains Python scripts for performing analysis:  
  - `age_box_chart_analysis.py` – Generates box plots to visualize age distribution.  
  - `age_scatter_plot_analysis.py` – Generates scatter plots to explore relationships in age data.  
  - `age_hypothesis_testing.py` – Performs statistical tests on age data.  
  - `rating_box_chart_analysis.py` – Generates box plots for movie ratings.  
  - `rating_scatter_plot_analysis.py` – Generates scatter plots for ratings analysis.  
  - `rating_hypothesis_testing.py` – Performs statistical tests on rating data.

- **`requirements.txt`**  
  Lists Python dependencies needed to run the project.



## 🛠️ How to Run the Project

1. **Clone the repository**
```bash
git clone <repository_url>
cd <repository_name>

```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Run the Analysis Scripts**

    All analysis scripts are located in the `src` folder. You can run them individually depending on the analysis you want to perform. Example commands:

```bash
# Age Analysis
python src/age_box_chart_analysis.py
python src/age_scatter_plot_analysis.py
python src/age_hypothesis_testing.py

# Rating Analysis
python src/rating_box_chart_analysis.py
python src/rating_scatter_plot_analysis.py
python src/rating_hypothesis_testing.py
```


# Analysis and Insights

## Age Analysis
- Visualizes the distribution of movie ages using box plots and scatter plots.
- Performs hypothesis testing to check if age-related trends are statistically significant.

## Rating Analysis
- Visualizes movie ratings distribution.
- Performs hypothesis testing to identify patterns and trends in ratings.



## 🔗 Dependencies
Key Python libraries used in this project:

- **pandas** – For data manipulation  
- **numpy** – For numerical computations  
- **matplotlib** – For plotting graphs  
- **seaborn** – For advanced visualizations  
- **scipy** – For statistical analysis  

All dependencies are listed in `requirements.txt`.



## 🎯 Objective
The main objectives of this project are:

- Examine how both platforms differ in terms of age-appropriate content distribution.  
- Perform hypothesis testing to determine whether there is a significant difference between the average user ratings and age restrictions of shows and movies on Netflix and Disney+.  
- Use data visualization techniques (box plots, scatter plots) to present insights and trends clearly.  
- Derive meaningful conclusions about content maturity, audience targeting, and platform-specific rating patterns.




##  License

This project is licensed under the terms of the [LICENSE](./LICENSE) file.

## 📌 Author
University Project by: [Kishlay Kumar](https://github.com/kishlaykumar990-hue)  
Course: Python Programming Assignment (DLMDSPWP01)








