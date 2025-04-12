from pydoc import describe

import pandas as pd


def main():
    # index_col indicates the first col (college names) are just labels
    college = pd.read_csv("../datasets/College.csv")
    college2 = pd.read_csv("../datasets/College.csv", index_col=0)

    college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
    college3 = college3.set_index('College')
    college = college3
    print(college.head(10))
    print(college.describe())


# Function only called when ran directly, not on import
if __name__ == '__main__':
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    print(bold_start + "\nRunning Chapter 2" + bold_end)
    print(
        bold_start + "====================================================================================================\n\n" + bold_end)
    main()
