 Data Analysis and Visualization using Python
This project demonstrates basic data inspection, handling missing values, and visualizations using a dataset (annual.csv) in Python with Pandas, NumPy, and Matplotlib.

📁 Files
File	Description
annual.csv	The dataset used for analysis
da1.py	Python script for loading, cleaning, and visualizing the dataset
Figure_1.png	Histogram image showing distribution of year values
output.png	Snapshot of Visual Studio Code terminal output (data summary, etc.)

🧪 Features of the Script (da1.py)
Basic Data Inspection:

Displays first 5 rows of the dataset

Prints dataset info (columns, datatypes, non-null counts)

Provides statistical summary

Checks for missing values

Missing Value Handling:

Numeric columns: filled with median

Categorical columns: filled with mode

Data Visualization:

Line plot of numeric values over years (if year column exists)

Histograms for numeric columns

Boxplots for numeric columns

▶️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install dependencies:

bash
Copy
Edit
pip install pandas matplotlib numpy
Run the script:

bash
Copy
Edit
python da1.py
📷 Sample Outputs
Histogram of Year:

Terminal Output:

📌 Requirements
Python 3.x

pandas

matplotlib

numpy

📝 License
This project is licensed under the MIT License.

