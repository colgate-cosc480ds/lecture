# Project

## Due Dates

Here are the *due dates* for key milestones:

- Weekly status reports: due **every Monday at 11:59pm** staring on 3/27.
- Proposal: **Monday, 3/27 11:59pm**
- Lab: Data acquisition lab on **Tuesday, 3/28**, due on **Monday, 4/3 11:59pm**
- Lab: Visualization lab on **Tuesday, 4/18**, due before class on **Wednesday, 4/19**
- Mini-presentation in class on **Wednesday, 4/19**.
- Final presentation: :tada: **Wednesday, 5/3 2:45-6:30pm** :tada: 
- Final report: **Tuesday, 5/9, 11:59pm**

## Guidelines

You are encouraged to work on teams of 2-3.

The goal of your project is to work with real data and employ the tools and methodology of data science to discover something interesting about your data.  

In the course we have discussed (or will be discussing) the key aspects of the data science process.  This includes:

- Data collection and processing: scraping, cleaning, wrangling, processing, querying using SQL, linking records between data sources, etc.
- Data exploration: using statistics and visualization to explore the data, observe outliers/anomalies, identify additional cleaning tasks.
- Data analysis: statistics, hypothesis testing, linear modeling
- Machine learning: prediction, clustering
- Visualization: plotting results

A complete project will use elements from all of these aspects of data science.  A high quality project will "go deep" along one or more of the above dimensions.  (For example, one project might involve a fairly intensive wrangling/cleaning of "wild" data; another project might start with a "clean" dataset but then perform an in-depth application of machine learning techniques to the dataset.)

*Alternative methods-based project* If you are more interested in studying the methods of data science, you could do a methods-oriented project.  Please come see me if you are interested in one of these projects.  An example of this kind of project would be taking a machine learning algorithm and adapting it so that it preserves the privacy of the individuals represented in the data.  


## Milestones

### Project proposal

Form a team.  Create a repo.  Identify the dataset(s) you want to study along with a list of potential questions you might explore.  Write a brief 1 paragraph description and commit it to the repo in a file called `proposal.md`.

### Weekly status reports

Each week, update the `weekly_status.md` file.  A template status report is provided.

### Lab: data acquisition and exploration

A lab will be devoted to project work on acquiring, cleaning and exploring your data.  The goal is data acquisition, cleaning, and exploration.  If you are starting out with raw or wild data, the deliverable will be something roughly akin to lab 1.  In other words, you will acquire your data, clean and prepare it, and start to explore it with some basic statistics and visualizations.

If you are starting from a "clean" dataset, you are expected to progress further.  For example, your work this week might resemble something more like lab3 in which you use SQL (or pandas or...) to do a deeper investigation of your data.

The deliverable is a python notebook that describes your data and the methodologies used to acquire, clean and prepare your data.  You may also need to update your `README.md` with installation instructions and instructions on how to obtain the source data.  *I should be able to run your python notebook in the VM and reproduce your results.*

### Lab: visualization

A lab will be devoted to generating interesting visualizations of your data.

The deliverable is a single PDF file containing one or more visualizations of your data.  You will share this visualization with the class during your mini-presentation.

### Mini presentation

Following the visualization lab, your team will be asked to give a brief (2 minute max!) presentation in class.  For this presentation, it is acceptable for one person to present on behalf of the group.  Your presentation should ideally include the visualization developed in the previous lab.  Share your work in progress with the rest of the class!

You must send me a PDF copy of any slides you wish to present *before* class.

### Final presentation

You are expected to give an oral presentation in which you describe the dataset, the problem or question you are exploring, a brief high-level overview of your methods, followed by a more in-depth discussion of your findings and conclusions.  Your presentation (powerpoint or its equivalent) should be rich with interesting visualizations of your data.

Plan on a 10 minute presentation.  Every time member is expected to participate in the presentation.

### Final report and repo commit

Your final deliverable is to commit your repo, which should contain your code and a final report.

**Repo** Your repo should have *all* of the code that you developed for your project along with instructions on how I can run your code to reproduce your findings.

**Report** In addition, your findings should be summarized in a final report.  The final report will be a self-contained document that contains the following sections:

- Introduction (1 page): Set the context (introduce the dataset and questions), provide *motivation* for why these are interesting questions to explore.  The introduction should end with a brief summary of your findings.
- Methodology (2 pages): Describe, at a high-level, the methods you employed.  Focus more attention on the more challenging/interesting/novel aspects.  Provide references to your code as appropriate.
- Related work (1/2 page): Briefly describe related work on this topic (if applicable).
- Results (2 pages): Present your findings through statistics, tables, and *visualizations*.
- Conclusions (1/2 page): Summarize the conclusions of your study.  This might include a discussion of future work.

The final report need not be long.  Concision is appreciated!  Some guideline page lengths are shown above.  (A notebook doesn't necessarily have "pages" but this guidelines should give you a rough idea.)

**Examples** For inspiration, here are some examples of very high quality, published research papers that follow roughly this template:

- [Friendship and Mobility: User Movement In
Location-Based Social Networks](http://cs.stanford.edu/people/jure/pubs/mobile-kdd11.pdf).
- [Discovering Value from Community Activity on Focused
Question Answering Sites: A Case Study of Stack Overflow](http://www.cs.cornell.edu/home/kleinber/kdd12-qa.pdf).
- [The Link Prediction Problem for Social Networks](http://www.cs.cornell.edu/home/kleinber/link-pred.pdf).

**Format** The *ideal* format for the final report is a python notebook.  The python notebook should include the appropriate calls to your code so that by running the python notebook, I can reproduce your results.  This may not be feasible in all cases (for example, if your project involves propietary data).  If it appears as though it may be difficult for your project, you **must** come see me well in advance of the project deadline to discuss.

You must also include any additional instructions in the project repo's `README.md`.  Instructions that should go here include any modifications to the VM, instructions on obtaining the source data, etc.



## Datasets

Here are some potential datasets you might consider.  You are free to find/use other datasets.

- Data from one of your own projects.  You are welcome and even encouraged to use data from another project (e.g., your senior thesis, your tech venture, etc.) but you must *clearly distinguish* between the work you are doing for this course from the work you are doing outside of this course.  (Your proposal would be a good place to start describing this distinction.)
- [Yelp Dataset](https://www.yelp.com/dataset_challenge/).
- Data from investigative studies of [biased algorithms](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) and other [investigative journalism](https://www.propublica.org/data/).
- [NYC Data from its stop and frisk police policy](http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml)
- Text data from [JStor](http://dfr.jstor.org/) (a repository of scientific literature)
- NYC Taxi data (big!)
- NYC Bike share data.
- Sports data, such as Basketball data [here](http://basketballvalue.com/downloads.php), [here](http://www.databasebasketball.com/stats_download.htm), and [here](http://www.sports-reference.com/data_use.html), or baseball [here](http://www.seanlahman.com/baseball-archive/statistics/) and [here](http://www.retrosheet.org/game.htm).
- Open government data (federal, state, municipal).  Example [open-gov](https://www.data.gov/open-gov/).
- Data on [Supreme court cases](http://scdb.wustl.edu/data.php).
- [US government spending data](https://www.usaspending.gov/Pages/Default.aspx) has information about government contracts and awards.
- [Govtrack](https://www.govtrack.us/developers) tracks all bills through the Congress and all votes casted by its members (and was used in a previous lab).
- Other lists of datasets:
	* [Washington post](http://www.washingtonpost.com/wp-srv/metro/data/datapost.html)
	* [KDD Nuggets](http://www.kdnuggets.com/datasets/index.html)
	* [NICAR Data Library](http://www.ire.org/nicar/database-library/)
	* [Google Fusion Tables](https://support.google.com/fusiontables/answer/2571232)
	* [Interesting data sets for statistics](http://rs.io/100-interesting-data-sets-for-statistics/)
- Data from data competitions (e.g., Kaggle)

