import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")
    total_people = df.shape[0]

    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    bachelors_degrees = df[df["education"] == "Bachelors"].shape[0]
    percentage_bachelors = round((bachelors_degrees / total_people) * 100, 1)

    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    higher_education_rich = round(
        higher_education[higher_education["salary"] == ">50K"].shape[0]
        / higher_education.shape[0]
        * 100,
        1,
    )
    lower_education_rich = round(
        lower_education[lower_education["salary"] == ">50K"].shape[0]
        / lower_education.shape[0]
        * 100,
        1,
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[
        (df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")
    ].shape[0]

    rich_percentage = (
        num_min_workers / df[df["hours-per-week"] == min_work_hours].shape[0]
    ) * 100

    # What country has the highest percentage of people that earn >50K?
    country_count = df["native-country"].value_counts()

    country_rich_counter = df[df["salary"] == ">50K"]["native-country"].value_counts()

    highest_earning_country = ((country_rich_counter / country_count) * 100).idxmax()
    highest_earning_country_percentage = round(
        ((country_rich_counter / country_count) * 100).max(), 1
    )

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        .groupby("occupation")["salary"]
        .count()
        .idxmax()
    )

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
