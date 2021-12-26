# Write your MySQL query statement below
select id, 
Sum(if(month = 'Jan', revenue, NULL)) AS Jan_Revenue,
Sum(if(month = 'Feb', revenue, NULL)) AS Feb_Revenue,
Sum(if(month = 'Mar', revenue, NULL)) AS Mar_Revenue,
Sum(if(month = 'Apr', revenue, NULL)) AS Apr_Revenue,
Sum(if(month = 'May', revenue, NULL)) AS May_Revenue,
Sum(if(month = 'Jun', revenue, NULL)) AS Jun_Revenue,
Sum(if(month = 'Jul', revenue, NULL)) AS Jul_Revenue,
Sum(if(month = 'Aug', revenue, NULL)) AS Aug_Revenue,
Sum(if(month = 'Sep', revenue, NULL)) AS Sep_Revenue,
Sum(if(month = 'Oct', revenue, NULL)) AS Oct_Revenue,
Sum(if(month = 'Nov', revenue, NULL)) AS Nov_Revenue,
Sum(if(month = 'Dec', revenue, NULL)) AS Dec_Revenue
from department group by id;