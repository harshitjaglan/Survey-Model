# Survey-Model


## Age Group: 
- Consider 4 groups as shown below


| Group                      | Group name | Age    |
| -------------------------- | ---------- | ------ |
| Elementary School Students | E          | 5 - 9  |
| Middle School Students     | M          | 10-14  |
| High School Students       | H          | 15-18  |
| College Students           | C          | 19-22  |


## Movie Genres

### Action
An action story is similar to adventure, and the protagonist usually takes a risky turn, which leads to desperate situations (including explosions, fight scenes, daring escapes, etc.).

### Science Fiction
Stories in this genre use scientific understanding to explain the universe that it takes place in.

### Comedy
Comedy is a story that tells about a series of funny, or comical events, intended to make the audience laugh.

### History
A story about a real person or event.

## Functionalty

Wrote a class named "Students" that has the following data attributes:
- Name: a string that contains the full name of the student.
- Age: an integer that holds the age information of the student.
- Movie genre: a list that contains the value either "YES" (if the student likes that genre) or "NO" otherwise.

The survey allows all students to enter their information through standard input.

Implemented the following functions:

1. `find_fav_genre(age_group)`: Takes an age group name as input and finds the favorite movie genre in that particular age group.

2. `calc_percentage_genre(age_group, genre)`: Takes an age group name and a specific movie genre as input and returns a list of percentages of students who like the movie genre in that particular age group.
