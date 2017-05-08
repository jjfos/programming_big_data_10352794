import pandas as pd
from commit import Commit
from datetime import date


def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data


def get_commits(data):
    #separate for each commit
    sep = 72*'-'

    commits = []
    current_commit = None
    index = 0

    author = {}
    while True:
        try:
            # parse each of the commits and put them into a list of commits
            current_commit = Commit()
            details = data[index + 1].split('|')
            current_commit.revision = int(details[0].strip().strip('r'))
            current_commit.author = details[1].strip()
            date = details[2].strip()
            date = date.split("+")
            current_commit.date = date[0].strip()
            current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
            current_commit.changes = data[index+2:data.index('',index+1)]
            index = data.index(sep, index + 1)
            current_commit.comment = data[index-current_commit.comment_line_count:index]
            commits.append(current_commit)
        except IndexError:
            break

    return commits;

#converting the commit list into a panda data frame
def get_data_frame(commits):

    # get labels for data frame columns
    labels = Commit.COLUMNS
    
    # holder commit data
    d=[]
    
    # iterate through commits to retrieve commit data
    for i, commit in enumerate(commits):
            temp = commits[i].get_commit()
            d.append(temp)

    # create dataframe
    df = pd.DataFrame(d, columns = labels)
    return df


# Analyse author data
def analazye_author_data(df):
   
    list_authors = df.author.unique()
    print("\nList of authors: " + str(list_authors))

    no_authors =df.author.nunique()
    print("\nNo of authors: " + str(no_authors))
  
    commits_per_author = df.groupby('author').size()
    print("\nCommits per Author")
    print(df.groupby('author').size())
    
    author_most_commits = df['author'].value_counts().idxmax()
    print("\nAuthor most commits: " + str(author_most_commits))

    author_least_commits = df['author'].value_counts().idxmin()
    print("\nAuthor least commits: " + str(author_least_commits))
   
    max_commits = commits_per_author.max()
    print("\nMaximum commits by author: " + str(max_commits))
    
    mean_commits =commits_per_author.mean()
    print("\nCommits mean:  " + str(mean_commits))
    
    median_commits = commits_per_author.median()
    print("\nCommits median: " + str(median_commits))



# Analyse comment data
def analazye_comment_data(df):
   
    mean_comments = df['comment line count'].mean()
    print("\nMean number of comment lines: " + str(mean_comments))
    
    median_comments = df['comment line count'].median()
    print("\nMedian number of comment lines: " + str(median_comments))

    max_lines_per_comment = df['comment line count'].value_counts().idxmin()
    print("\nMost number of lines per comment: " + str(max_lines_per_comment))
    
    min_lines_per_comment = df['comment line count'].value_counts().idxmax()
    print("\nLeast number of lines per comment: " + str(min_lines_per_comment))


# Analyse date data
def analazye_date_data(df):

    df['date'] = pd.to_datetime(df['date'])
    dates = df.groupby([df.date.dt.year, df.date.dt.month, df.date.dt.day]).size()
    no_dates = dates.count();
    print("\nNumber of dates: " + str(no_dates))
    
    most_commits_per_date = dates.max()
    print("\nMost commits on a day: " + str(most_commits_per_date))
    
    date_most_commits = dates.idxmax()
    print("\nDate of most commits: " + str(date_most_commits))


def get_no_authors(df):
    return df.author.nunique();

def get_no_dates(df):
    df['date'] = pd.to_datetime(df['date'])
    dates = df.groupby([df.date.dt.year, df.date.dt.month, df.date.dt.day]).size()
    return dates.count();

def get_most_lines_per_comment(df):
    return df['comment line count'].value_counts().idxmin()


if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    df = get_data_frame(commits)

    #generate different analysis
    analazye_author_data(df)
    analazye_comment_data(df)
    analazye_date_data(df)






