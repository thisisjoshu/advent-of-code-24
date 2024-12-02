import pandas as pd


def main():

    # read input file
    # put
    # sort both dfs from smallest to largest
    # match indices of each df
    # get diff_dference and store in a separate df
    # sum the third df

    df = pd.read_csv("input.csv")

    left_df = df["left"]
    right_df = df["right"]

    left_df = left_df.sort_values(ascending=True, ignore_index=True)
    right_df = right_df.sort_values(ascending=True, ignore_index=True)

    diff_df = (left_df - right_df).abs()
    total = diff_df.sum()
    print(total)

    # get the number of times number on the left appears on the right
    # multiply that number with the number on the left (similarity score)
    # sum up the similarity score

    occurrences = right_df.value_counts()

    similarity_scores = left_df.apply(lambda x: x * occurrences.get(x, 0))

    total_similarity_score = similarity_scores.sum()
    print(total_similarity_score)


if __name__ == "__main__":
    main()
