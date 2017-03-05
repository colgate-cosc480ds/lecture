# Lecture Schedule

## Introduction

- Mon, Jan 23 Lecture 1:  Half-day introduction.
    + Reading: syllabus
- Wed, Jan 25 Lecture 2: Introduction.
    + Reading: DSFS Ch. 1-4. (Read these 4 chapters sometime this week.  Ch. 2 and 3 are important for next week's lab.)
    + Reading: Read the following article: [Detecting influenza epidemics using search engine
query data](http://www.nature.com/nature/journal/v457/n7232/pdf/nature07634.pdf).  **Come to class prepared to discuss it.**  In particular, do the following:
        * Review the "Process of Data Science" slide from the first day's lecture.  Slides are available in this repo.  Align those steps with what was done in this study.  
        * Are any steps missing (or at least not discussed in this article)?
        * The paper describes the model they used for this data.  What is the model?  (I realize some terminology may be unfamiliar, but do your best to try to make sense of it.)
        * Think critically about GFT.  What problem is it attempting to solve?  Is it an effective solution?  What are some potential limitations?


## Data Processing

- Mon, Jan 30 Lecture 3: Data acquisition, cleaning, exploration.
    + Reading:
        * DSFS Ch. 9 Getting Data
        * DSFS Ch. 10 Working with Data (Exploring Your Data, p. 121-127)
        * DSFS Ch. 10 Working with Data (Cleaning and Munging, p. 127-129)
        * DSFS Ch. 10 Working with Data (Manipulating Data, p. 129-132)
        * [Python Regexp Tutorial](https://developers.google.com/edu/python/regular-expressions)
        * Supplemental: [another regexp tutorial](https://docs.python.org/2/howto/regex.html), docs for python [re module](https://docs.python.org/2/library/re.html#module-re)    
- Wed, Feb 01 Lecture 4:  Data processing.
    + Reading: 
        * Supplementary: Ch. 12.4 of Boat book.  Available [via moodle](https://moodle.colgate.edu/mod/resource/view.php?id=197855)
- Mon, Feb 06 Lecture 5:  Manipulating Tabular Data (SQL).
    + Reading: 
        * *I'm going to assign several different readings related to SQL.  You don't need to read all of it in fine detail.  Below I annotate each reading with what you should get out of it.  You can also use my lectures as a guide -- if I don't mention it in lecture, I won't hold you accountable for knowing it.*
        * DSFS Ch. 23 Databases and SQL -- *This provides a fairly quick overview of SQL and even uses python code to illustrate what each sql operation does.  This is a good place to start but it is missing useful features, such as the WITH keyword.*
        * [Boat book, Ch. 2](https://moodle.colgate.edu/mod/resource/view.php?id=195388) -- *This provides a basic overview of the relational model.  This should be a quick read.  If you come out of this chapter knowing the following concepts -- relation, schema, key -- you're probably good.*
        * [Boat book, Ch. 3](https://moodle.colgate.edu/mod/resource/view.php?id=195389) -- *This is a useful reference for SQL.  Sections 3.5 and 3.6 are less important.  Section 3.7 is essential.  Section 3.8 is about subqueries.  For this course, it probably suffices to focus on Section 3.8.6, which describes the WITH clause, a super useful feature.*
- Wed, Feb 08 Lecture 6:  Manipulating Tabular Data (SQL continued / Pandas)
    + Reading: 
        * The pandas library is a useful library for manipulating data in Python.  A book on it is available on moodle and I think the following chapter is the most useful.  It's unlikely that we will spend a lot of time on it in this course -- we simply don't have time and I want to focus on more fundamental, established languages like SQL.  However, I do want to bring it to your attention as a useful tool.  Therefore, consider this reading more as a reference rather than required reading.  The parts of pandas that I will expect you to know will be only those that I mention in class.
        * *Reference*: [Ch. 5 of Python for Data Analysis](https://moodle.colgate.edu/mod/url/view.php?id=194037)
- Mon, Feb 13 Lecture 7:  Fuzzy matching.
    + Reading: *TBD*

## Computational Statistics

- Wed, Feb 15 Lecture 8: Statistics
    + Reading: 
        * DSFS Ch. 5 Statistics (*You may want to review DSFS Ch. 4, which covers some linear algebra concepts that come up in this chapter, like dot.*)
        * [Simpspon's Paradox](http://vudlab.com/simpsons/)
- Mon, Feb 20 Lecture 9: Probability
    + Reading: 
        * DSFS Ch. 6 Probability
        * Supplemental: [Chances Are](https://opinionator.blogs.nytimes.com/2010/04/25/chances-are/)
- Wed, Feb 22 **Quiz 1** (in class)
    + *You will have the entire class period to complete the quiz though I expect you will finish in much less time than that.*
- Mon, Feb 27 Lecture 10: Probability, continued... 
    + Reading: Review DSFS Ch. 6
- Wed, Mar 01 Lecture 11: Hypothesis Testing
    + Reading: DSFS Ch. 7 Hypothesis and Inference
- Mon, Mar 06 Lecture 12: Linear Regression I & Gradient Descent
    + Reading: 
        * DSFS Ch. 14 Simple Linear Regression 
        * DSFS Ch. 8 Gradient Descent
    + Questions
        * Which of the following are differences between gradient descent (GD) and stochastic gradient descent (SGD)?
            - GD is regular gradient descent whereas SGD adds random noise to the gradient to help avoid local minima/maxima
            - SGD is preferred for large datasets
            - SGD requires an *additive* target function
        * What is the role of step size in GD or SGD?  How do you choose the "right" step size?
        * In simple linear regression, given values for `alpha` and `beta` and a small dataset (say 3 data points), you should be able to compute how well the model fits the data.
        * Taking Ch. 8 and Ch. 14 together, the book offers three different ways to fit a simple linear regression model.  What are they?
        * If you were to use GD to fit a simple linear regression model, what would the target function `target_fn` be?


- Tue, Mar 07 **Quiz 2** (in lab)
- Wed, Mar 08 Lecture 13: Linear Regression II
    + Reading: 
        * DSFS Ch. 15 Multiple Regression
- Mon, Mar 13 **No class: spring break!**
- Wed, Mar 15 **No class: spring break!**

## Machine Learning

- Mon, Mar 20 Lecture 14: Overview of Machine Learning
    + Reading: DSFS Ch. 11 Machine Learning
- Wed, Mar 22 Lecture 15: Classification: Linear Disciminants, Perceptron, Logistic Regression
    + Reading: DSFS Ch. 16 Logistic Regression 
- Mon, Mar 27 Lecture 16: k-NN and trees
    + Reading: 
    	* DSFS Ch.12 k-NN
    	* DSFS Ch.17 Decision Trees
- Wed, Mar 29 Lecture 17: Learning Theory
    + Reading: *TBD*
- Mon, Apr 03 Lecture 18: Overfitting
    + Reading: *TBD*
- Wed, Apr 05 Lecture 19: *TBD*

## Visualization

- Mon, Apr 10 Lecture 20: Visualization I
    + Reading: *TBD* 
- Wed, Apr 12 Lecture 21: Visualization II
    + Reading: *TBD*

## Additional Topics

- Mon, Apr 17 Lecture 22: Network Analysis
    + Reading: *TBD*
- Wed, Apr 19 Lecture 23: Streaming Data
    + Reading: *TBD*
- Fri, Apr 21: NASC Colloquium Talk: *Data Analysis with Privacy Protection: Seeing the Forest But Not The Trees*
	+ You are **required** to attend this event.
- Mon, Apr 24 Lecture 24: Privacy I
    + Reading: *TBD*
- Wed, Apr 26 Lecture 25: Privacy II
    + Reading: *TBD*
- Mon, May 01 Lecture 26: Fairness
    + Reading: *TBD*
- Wed, May 03 Lecture 27: :tada: **Project Presentations 2:45 - 6:30pm** :tada:
	+ *Please do not make any commitments during this time window*
- Tue, May 09 **Final Exam** time slot: 12:00 - 2:00pm.  *Hold for last quiz*
- Tue, May 09 **Final Project Report Due** 
