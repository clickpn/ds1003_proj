## User Guide
- DS-GA-1003  Final Project: Legal Outcome Prediction
- Advisor: Dr.Daniel Chen
- Team Member:
  - Muhe Xie(mx419) mx419@nyu.edu
  - Sida Ye(sy1743) sy1743@nyu.edu
  - Xingye Zhang(xz601) xz601@nyu.edu

Note: You can run the commands in Part 4 directly to get the result. But you can read the following parts to understading the process.

### Part 0: Environment Setup
1. run the following commands to download our projects
``` sh
$ git clone [git-repo-url]
$ cd code
```

### Part 1: File Description
1. code: contains all code and data we used in this project
2. poster: contains poster we used in poster session
3. report: contains final report

### Part 2: Data Clean, Merge

1.  Merge 100Votelevel_touse.dta, sunstein_data_for_updating.csv and bigfile.csv to get dataframe with caseid, panel vote and legal field.
    * We have 100Votelevel_touse.dta, which contains case_id (start with X) and citation. We also have sunstein_data_for_updating.csv, which contains citation and issue, which represent legal fields.  After merging these two files on citation, we got 2526 records with case_id, citation and issue in columns. By citation and issue, we then get dataframe with case_id, citation, issue and its corresponding panel vote. We also delivery a target case id list for matching caseid in Vocab_map_text file.
    * It will delivery a dataframe called init_df.

2. Clean Vocab_map_text file.
    * Finding target case id list from step 1. It will convert the original vocab_map_txt file format into (word_id, n-gram dictionary) format.
    * It will delivery a target_ngram_df.

3. Merge init_df, target_ngram_df. We then get our final_df.csv which contains case_id, n-gram, panel_vote, issue(int) and legal field(string).
```sh
python merge_data.py
```

### Part 3: Feature Selection

1. Spilt the final_df.csv into 16 dataframe based on the legal fields.

2. Reduce the dimension of each dataframe. 

```sh
python feature_selection.py
```
It will generate 16 csv files corresponding to each legal fields under ./code/field/ directory.


### Part 4: Modeling and Generating Key Word Features
This part will use dataframe from part4 feature selection. We also check the correlation between panelvote and x_dem in Circuit_Cases. If the correlation is postive, we would like to consider panel vote with 2,3 as liberal which is 1.

1. Find target word feature id
``` sh
python word_generate.py
```
It will save a pickle file, which contains the target word id list we need to find in Vocab_map_text file.

2. Match targe word feature id with its real ngram

3. Run the following command, which will generate the AUC performance for each legal field and positive, negative word list in terminal.
``` sh
python modeling.py
```
If you want to save the result, you can run
``` sh
python modeling.py > result.txt
```

### Acknowledgement
- Law Data resource from Daniel Chen
