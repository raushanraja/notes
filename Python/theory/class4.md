  
  
# Numpy
  
  
## Methods
  
  
+ mean( ) : For mean
+ std( ) : For standard deviation, variation of data from mid data point
+ var( )
  
|Method|Function|Formaula|
|---|---|---|---|
|<img src="https://latex.codecogs.com/gif.latex?mean(%20&#x5C;%20)"/>|For calculating mean/average| <img src="https://latex.codecogs.com/gif.latex?(x1+x2+...+xn)&#x2F;n"/>|
|<img src="https://latex.codecogs.com/gif.latex?std(%20&#x5C;%20)"/>|For calculating standard deviation| <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{%20(&#x5C;sum%20x-mean(x))&#x2F;n}"/>|
|<img src="https://latex.codecogs.com/gif.latex?var(%20&#x5C;%20)"/>|For calculating mean/average| <img src="https://latex.codecogs.com/gif.latex?(&#x5C;sum%20x-mean(x))&#x2F;n"/>|
  
# Pandas
  
  
  
|Methods|Function||
|--|--|--|
|<img src="https://latex.codecogs.com/gif.latex?DataFrame(&#x5C;%20)"/>| For creating a dataframe from the data||
|<img src="https://latex.codecogs.com/gif.latex?head(&#x5C;%20)"/>| shows top 5 data ||
|<img src="https://latex.codecogs.com/gif.latex?tail(&#x5C;%20)"/>| shows last 5 data||
|<img src="https://latex.codecogs.com/gif.latex?describe(&#x5C;%20)"/>| for calculation summary by calculating mean,std,min,25% ,50% ,75%,max||
|<img src="https://latex.codecogs.com/gif.latex?isnull(&#x5C;%20)"/>|return false is data is present in column or true||
|<img src="https://latex.codecogs.com/gif.latex?dropna(&#x5C;%20)"/>|removes the row or column if nan is present ||
|<img src="https://latex.codecogs.com/gif.latex?fillna(&#x5C;%20a&#x5C;%20%20)"/>|fills the row or column if nan is present with specified value of <img src="https://latex.codecogs.com/gif.latex?a"/> ||
|<img src="https://latex.codecogs.com/gif.latex?shape"/>| shows number of rows and columns||
|<img src="https://latex.codecogs.com/gif.latex?to&#x5C;_csv(&#x5C;%20)"/>| to save dataframe to a csv file||
  
### Access columns
  
  
+ **<img src="https://latex.codecogs.com/gif.latex?df[&#x27;column&#x5C;_name&#x27;]"/>**   : to get the specified column only
+ **<img src="https://latex.codecogs.com/gif.latex?df.column&#x5C;_name"/>**      : to get the specified column only
  
#### dropna()
  
  
+ dropna(how='any')  // removes even if 1 value is nan
+ dropna(how='all')  // removes only all values are nan
  
#### fillna()
  
  
+ dropna(0,inplace=True) // Updates the dataframe
  
  
#### Accessing elements
  
  
+ df.<img src="https://latex.codecogs.com/gif.latex?iloc[a:b,c:d]"/> : to access the elements (rows & columns) based on index.
  
  + <img src="https://latex.codecogs.com/gif.latex?a:b=start&#x5C;%20row:&#x5C;%20end%20&#x5C;%20row"/> ,
  +  <img src="https://latex.codecogs.com/gif.latex?c:d=start&#x5C;%20column:end&#x5C;%20column"/>,
  + <img src="https://latex.codecogs.com/gif.latex?iloc[::]"/> : All rows and columns
  + <img src="https://latex.codecogs.com/gif.latex?iloc[i]"/> : <img src="https://latex.codecogs.com/gif.latex?i^{th}"/> row and all column
  + <img src="https://latex.codecogs.com/gif.latex?iloc[:i]"/> :  all row and all column  utpo <img src="https://latex.codecogs.com/gif.latex?i^{th}"/> row
  + <img src="https://latex.codecogs.com/gif.latex?iloc[i:j]"/> :  all row and all column  from <img src="https://latex.codecogs.com/gif.latex?i^{th}"/> row toc<img src="https://latex.codecogs.com/gif.latex?j^{th}"/> row
  + <img src="https://latex.codecogs.com/gif.latex?iloc[:,j]"/> :  all row and <img src="https://latex.codecogs.com/gif.latex?j^{th}"/> column
  + <img src="https://latex.codecogs.com/gif.latex?iloc[:,i:j]"/> :  all row and  column  from <img src="https://latex.codecogs.com/gif.latex?i^{th}"/> column to <img src="https://latex.codecogs.com/gif.latex?j^{th}"/> column
  
  