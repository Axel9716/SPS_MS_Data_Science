# Alex Ptacek - QOTW #10

# 1. What is matplottlib and seaborn?  When would you choose one over the other?

# Answer: Matplotlib and Seaborn are both data visualization packages in Python. 
# Seaborn is built on top of Matplotlib. Matplotlib naturally gives access to more 
# granular plot composition, while Seaborn is a bit more high-level and easier to use.



# 2. Image you are creating a visualization for a presentation at work.  What are some recommendations or guidelines you would follow to make engaging and informative visuals?

# Answer: The most important thing is that the visualization tells a story. At work, I always analyze data in many different views so that I can get a bigger picture
# and try to answer any questions that arise by looking at a different view. Visualizations can help guide this questioning (e.g. EDA), but for presenation we should
# use visualizations to show the "answer" that we found. It's also important to choose the right type of graph and don't clutter it too much.


# 3. Give an example of either a matplotlib or seaborn graphic (give code).  You may also reference an informative article.

import seaborn as sns
import matplotlib.pyplot as plt

# tips dataset comes with the seaborn package
df = sns.load_dataset('tips')

# Create a scatter plot with regression line
sns.lmplot(x='total_bill', y='tip', data=df, height=5, aspect=1.2)

plt.title('Relationship Between Total Bill and Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.tight_layout()
plt.show()


# 4. Link does not work 