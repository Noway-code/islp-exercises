import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import boxplot


def main():
    # index_col indicates the first col (college names) are just labels
    college = pd.read_csv("../datasets/College.csv")
    college2 = pd.read_csv("../datasets/College.csv", index_col=0)

    college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
    college3 = college3.set_index('College')
    college = college3
    # print(college.head(10))
    # print(college.describe())

    pd.plotting.scatter_matrix(college[["Top10perc", "Apps", "Enroll"]])
    # plt.show()

    # Out-state students based on private or not.
    college.boxplot(column="Outstate", by="Private")
    plt.title("Outstate vs Private")
    plt.suptitle("")  # Remove the default subtitle
    plt.xlabel("Private")
    plt.ylabel("Outstate")
    plt.show()
    college['Elite'] = pd.cut(college['Top10perc'],
                              [0, 50, 100],
                              labels=['No', 'Yes'])
    print(college['Elite'].value_counts())
    # Out-state students based on private or not.
    college.boxplot(column="Outstate", by="Elite")
    plt.title("Outstate vs Elite")
    plt.suptitle("")  # Remove the default subtitle
    plt.xlabel("Elite")
    plt.ylabel("Outstate")
    plt.show()


# Function only called when ran directly, not on import
if __name__ == '__main__':
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    print(bold_start + "\nRunning Chapter 2" + bold_end)
    print(
        bold_start + "====================================================================================================\n\n" + bold_end)
    main()
