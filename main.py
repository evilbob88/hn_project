#!/usr/bin/env python
# coding: utf-8

from csv import reader
opened_file = open('hacker_news.csv', encoding="utf8")
read_file = reader(opened_file)
list_file = list(read_file)

hn = list_file

hn_headers = hn[0]
hn_data = hn[1:]

print(hn_data[:5])

ask_posts = []
show_posts = []
other_posts = []

for row in hn_data:
    title = row[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(row)
    elif title.lower().startswith("show hn"):
        show_posts.append(row)
    else:
        other_posts.append(row)

num_ask = len(ask_posts)
num_show = len(show_posts)
num_other = len(other_posts)

print("There are {} ask posts.".format(num_ask))
print("There are {} show posts.".format(num_show))
print("There are {} other posts.".format(num_other))

total_ask_comments = 0

for post in ask_posts:
    num_comments = post[4]
    total_ask_comments += int(num_comments)

avg_ask_comments = total_ask_comments / num_ask

print("There are a total of {:,} comments in {:,} ask posts, an average of {:.2f} comments per row.".format(total_ask_comments, num_ask, avg_ask_comments))

total_show_comments = 0

for post in show_posts:
    num_comments = post[4]
    total_show_comments += int(num_comments)

avg_show_comments = total_show_comments / num_show
print("There are a total of {:,} comments in {:,} show posts, an average of {:.2f} comments per row.".format(total_show_comments, num_show,avg_show_comments))

import datetime as dt

result_list = []

for post in ask_posts:
    created_at = post[6]
    result_list.append([created_at, int(post[4])])

counts_by_hour = {}
comments_by_hour = {}
date_format = "%m/%d/%Y  %H:%M"

for row in result_list:
    date = row[0]
    comment = row[1]
    hour = dt.datetime.strptime(date, date_format).strftime("%H")
    if hour in counts_by_hour:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += comment
    else:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = comment

print(counts_by_hour)
print(comments_by_hour)

avg_comments = []

for hour in comments_by_hour:
    avg_comments.append([hour, round(comments_by_hour[hour] / counts_by_hour[hour], 2)])

print(avg_comments)

swap_avg_by_hour = []

for hour in avg_comments:
    swap_avg_by_hour.append([hour[1], hour[0]])

sorted_swap_desc = sorted(swap_avg_by_hour, reverse=True)

print("Top 5 Hours for Ask Post Comments")

for row in sorted_swap_desc[:5]:
    print("{}:00: {:.2f} average comments per post".format(row[1], row[0]))

print("\n")

sorted_swap_asc = sorted(swap_avg_by_hour)

print("Bottom 5 Hours for Ask Post Comments")

for row in sorted_swap_asc[:5]:
    print("{}:00: {:.2f} average comments per post".format(row[1], row[0]))

