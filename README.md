# **MiniProject2**

![Build Status](https://travis-ci.org/cen24/miniproject2.svg?branch=master)

Created a python module to perform statistical calculations. For each calculation we created at least one test to check for the correct value and another test to check for invalid input. Invalid input would throw an exception with a description of the problem.

See below for calculations that can be performed.

### **Program calculates the following:**

- [X] Population Mean - formula, = μ = ( Σ Xi ) / N.
The mean is the usual average, so I'll add and then divide:

(13 + 18 + 13 + 14 + 13 + 16 + 14 + 21 + 13) ÷ 9 = 15

Note that the mean, in this case, isn't a value from the original list. This is a common result. You should not assume that your mean will be one of your original numbers.

- [X] Median - formula, Size of (n+12)th item

The median is the middle value, so first I'll have to rewrite the list in numerical order:

13, 13, 13, 13, 14, 14, 16, 18, 21

There are nine numbers in the list, so the middle one will be the (9 + 1) ÷ 2 = 10 ÷ 2 = 5th number:

13, 13, 13, 13, 14, 14, 16, 18, 21

So the median is 14.

- [X] Mode  - formula, The mode is that value in a series of observation which occurs with greatest frequency. 

list - 13, 13, 13, 13, 14, 14, 16, 18, 21

The mode is the number that is repeated more often than any other, so 13 is the mode from the list above

The largest value in the list is 21, and the smallest is 13, so the range is 21 – 13 = 8.


- [X] Population Standard Deviation  - formula,  σ = sqrt [ Σ ( Xi - μ )2 / N ]

- [X] Variance of population proportion  - formula, σP2 = PQ / n.

- [x] Z-Score/Standardized Score  - formula, Z = (X - μ) / σ

- [X] Population Correlation Coefficient - Correlation coefficients are used in statistics to measure how strong a relationship is between two variables. There are several types of correlation coefficient: Pearson’s correlation (also called Pearson’s R) is a correlation coefficient commonly used in linear regression.

- [X] Confidence Interval  - Statisticians use a confidence interval to express the degree of uncertainty associated with a sample statistic. A confidence interval is an interval estimate combined with a probability statement.

For example, suppose a statistician conducted a survey and computed an interval estimate, based on survey data. The statistician might use a confidence level to describe uncertainty associated with the interval estimate. He/she might describe the interval estimate as a "95% confidence interval". This means that if we used the same sampling method to select different samples and computed an interval estimate for each sample, we would expect the true population parameter to fall within the interval estimates 95% of the time.

- [x] Population Variance  - formula, σ2 = Σ ( Xi - μ )2 / N.

- [x] Sample Variance  - formula, s2 = Σ ( xi - x )2 / ( n - 1 )

- [x] P Value  - formula, p-value = P(TS ts. H 0 is true) = cdf(ts)
The p-value is calculated using the sampling distribution of the test statistic under the null hypothesis, the sample data, and the type of test being done (lower-tailed test, upper-tailed test, or two-sided test). The p-value for: a lower-tailed test is specified by the formula above.

- [X] Proportion  - A proportion is simply a statement that two ratios are equal. It can be written in two ways: as two 
equal fractions a/b = c/d; or using a colon, a:b = c:d.

- [x] Sample Mean  - formula, x = ( Σ xi ) / n

- [X] Sample Standard Deviation  - formula, s = sqrt [ Σ ( xi - x )2 / ( n - 1 ) ]

- [X] Variance of sample proportion  - formula, sp2 = pq / (n - 1)

**For definitions of some of the programming terms used please see link below for their definitions  :** [Additional terms(miniproject2)](https://github.com/rutvik2611/miniproject1/blob/master/Additional%20terms(miniproject2).md)

### Contributors
1. [Chinedu Nnaji](https://www.linkedin.com/in/chinedunnaji/), Cen24 (UCID)
2. [Rutvik Patel](https://github.com/rutvik26110), RP883 (UCID)

### Reference
1. https://www.wallstreetmojo.com/p-value-formula/

2. http://www.differencebetween.net/science/difference-between-sample-mean-and-population-mean

3. https://docs.python.org/3/library/statistics.html

### Change log
See link for complete log: [Log.csv](./log.csv)

|Hash   |User |Date/Time            |Change                                                                                                                          |
|-------|-----|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
6daa95b|rutvik2611|Sun Nov 10 16:06:07 2019 -0500|Fix:Use split function for Varaince of sample proportion
2ee55fb|rutvik2611|Sun Nov 10 16:04:37 2019 -0500|Fix:Use split function for sample mean and sample stdev
aaa48eb|rutvik2611|Sun Nov 10 16:04:08 2019 -0500|Fix:Update Result and test case
e8e10a7|rutvik2611|Sun Nov 10 16:03:37 2019 -0500|Feature:Made a splut list function for sample
7d08b37|ChineduN|Sun Nov 10 01:24:53 2019 -0500|fix : read me
74a383c|Chinedu Nnaji|Sun Nov 10 01:23:24 2019 -0500|fix : read me and deleted vpop and samppop
01054bf|rutvik2611|Sat Nov 9 20:46:24 2019 -0500|Fix:Median Test
