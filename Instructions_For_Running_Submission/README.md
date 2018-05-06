# Final Project

<h2> Running the project: </h2>

<h4> Requirements:</h4>

Python (version >= 2.7)

<h4> Get the python server up and running:</h4>
Set up a python server using one of the following two commands based on the python version installed on your computer:
<h5> If Python version is 3.X </h5>
<h6> python -m http.server </h6>

<h5> If Python version is 2.X </h5>
<h6> python -m SimpleHTTPServer </h6>

In your web browser, type in localhost:8000 and the dashboard with the three visualizations can be viewed. 

<h4> Visualizations on the dashboard </h4>
The first visualization has a bubble graph that indicates the clustering of the posts in a subreddit by topic. The size of the bubbles indicates average karma of posts in corresponding topics. You can switch back and forth between subreddits by means of a drop-down menu.


The second visualization shows a stacked bar chart indicating the number of posts per subreddit. The stacks indicate proportion ofthe posts per subreddit which were above or below the Karma threshold selected by the viewer.


The third visualization indicates a line graph that shows temporal information about the mean Karma normalized by the number of users. This includes semantic zooming where this information can be obtained at the level of the entire week or the viewer could select a particular day in a week to see how the Karma varies over the course of the day. The views can be switched between time scales and subreddits by means of drop down menus.

<h4> Analysis of  visualizations </h4>

Further description and analyses of the visualization has been documented in the final paper. This can be accessed in the folder in the main repository titled FinalProject_WriteUp. Both .pdf and .docx versions of the write up are available in this folder. 
