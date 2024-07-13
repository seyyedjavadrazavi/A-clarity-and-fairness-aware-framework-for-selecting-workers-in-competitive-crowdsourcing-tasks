# A Clarity and Fairness Aware Framework for Selecting Workers in Competitive Crowdsourcing Tasks

## Introduction
This repository contains the code for the article "A Clarity and Fairness Aware Framework for Selecting Workers in Competitive Crowdsourcing Tasks." Follow the steps below to run the code.

## 0. Download Dataset
We used the Stack Overflow dataset. You can download it from [this link](https://drive.google.com/drive/folders/1q33zXpglbViJtDEJYP0oAuH-r24wkWKU?usp=sharing). Then you must put each file in the corresponding directories on the 1_prepration folder. For example, you should put the Posts.xml in the 1_prepration/posts folder.

## Progress
To use this code for your purposes and dataset, follow and run the files in order based on their numbers. Each folder is named with a number to indicate the sequence, from `1_preparation` to `13_charts`. Within each folder, if order matters, the files follow a similar pattern; otherwise, you can run them in any order. Detailed instructions for each section are provided below.

## 1. Preparation
First, convert XML files to CSV files by running the code in the `1_preparation` folder. Paths are relative, and all files will be stored next to their corresponding Python code.

## 2. Requester Profile
Create profiles for requesters, tasks (works), and workers. To create requesters' profiles, run the following scripts:

```sh
cd 2_requester_profile
python3 1_user_profile.py
python3 2_indices_of_tags.py
```

## 3. Work Profile
To create work profiles, change the directory to the `3_work_profile` folder and run the script below:

```sh
python3 work_info.py
```

## 4. Worker Profile
To get workers' profiles, change the directory to the `4_worker` folder and run the scripts below:

```sh
python3 1_worker_profile.py
python3 2_get_index_of_not_null_tags.py
```

## 5. Correlation
To compute the correlation between different dataset features, run the Python files in the `5_correlation` folder.

## 6. Fairness
In this directory, there are two folders: `candidate` and `community_score`. Run the following scripts in each folder:

**Candidate Folder:**

```sh
python3 1_acan_score_rate.py
python3 2_candidate_acan.py
```

**Community Score Folder:**

```sh
python3 comm_score.py
```

## 7. Clarity
In the `clarity` folder, you'll find fuzzy rules in a Word file. To compute clarity, change the directory to the `fuzzy_model` folder and run the script below:

```sh
python3 computeClarity.py
```

## 8. Similar Works to End
From here to the end, run the folders and files in order. Use the scripts below:

```sh
cd 8_similar_works
python3 1_comb_jaccard_similarity.py
python3 2_get_index_of_not_null_tags.py
python3 3_select_test_data_index.py
python3 4_similar_work.py
python3 5_moreThan30.py

cd ..
cd 9_test_data
python3 1_create_test_data.py
python3 2_add_original_workers_to_testdata.py

cd ..
cd 10_train_data
python3 comb_intersection_similarity.py

cd ..
cd 11_ML
python3 new_mlp_RobustScaler.py

cd ..
cd 12_suitability_score
python3 compWithOriginal_top_50.py

cd ..
cd 13_metrics
cd all_tag
python3 rbp_all_tag.py

cd ..
cd each_tag
python3 rbp_each_Tag.py

cd ..
cd ..
cd 14_charts
python3 1_dist.py
```

## Note
For any questions, feel free to open an issue or email [javad.b.razavi@gmail.com](mailto:javad.b.razavi@gmail.com).
