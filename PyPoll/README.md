# PyPoll Challenge

In this challenge, I was tasked with helping a small, rural town modernize its vote counting process.

I was given a set of poll data called [election_data.csv]. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". My task was to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

MY analysis output needed to look similar to the following:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

In addition, my final script needed to both print the analysis to the terminal and export a text file with the results.
