---
markdown:
  image_dir: /assets
  path: class4.md
  ignore_from_front_matter: true
  absolute_image_path: false
export_on_save:
  markdown: true
---

# Numpy

## Methods

+ mean( ) : For mean
+ std( ) : For standard deviation, variation of data from mid data point
+ var( )

|Method|Function|Formaula|
|---|---|---|---|
|$mean( \ )$|For calculating mean/average| $(x1+x2+...+xn)/n$|
|$std( \ )$|For calculating standard deviation| $ \sqrt{ (\sum x-mean(x))/n} $|
|$var( \ )$|For calculating mean/average| $ (\sum x-mean(x))/n $|

# Pandas

  
|Methods|Function||
|--|--|--|
|$DataFrame(\ )$| For creating a dataframe from the data||
|$head(\ )$| shows top 5 data ||
|$tail(\ )$| shows last 5 data||
|$describe(\ )$| for calculation summary by calculating mean,std,min,25% ,50% ,75%,max||
|$isnull(\ )$|return false is data is present in column or true||
|$dropna(\ )$|removes the row or column if nan is present ||
|$fillna(\ a\  )$|fills the row or column if nan is present with specified value of $a$ ||
|$shape$| shows number of rows and columns||
|$to\_csv(\ )$| to save dataframe to a csv file||

### Access columns

+ **$df['column\_name']$**   : to get the specified column only
+ **$df.column\_name$**      : to get the specified column only

#### dropna()

+ dropna(how='any')  // removes even if 1 value is nan
+ dropna(how='all')  // removes only all values are nan

#### fillna()

+ dropna(0,inplace=True) // Updates the dataframe


#### Accessing elements

+ df.$iloc[a:b,c:d]$ : to access the elements (rows & columns) based on index.
  
  + $a:b=start\ row:\ end \ row$ ,
  + $c:d=start\ column:end\ column$,
  + $iloc[::]$ : All rows and columns
  + $iloc[i]$ : $i^{th}$ row and all column
  + $iloc[:i]$ :  all row and all column  utpo $i^{th}$ row
  + $iloc[i:j]$ :  all row and all column  from $i^{th}$ row toc$j^{th}$ row
  + $iloc[:,j]$ :  all row and $j^{th}$ column
  + $iloc[:,i:j]$ :  all row and  column  from $i^{th}$ column to $j^{th}$ column
  + **divisible by 2:**  $df.iloc[lambda\  x:x\%2==0]$

# Matplotlib

+ 2-d visualization libraby
+ $import \ matplotlib.pyplot\ as\ plt$
  
>   ```python
>      plt.scatter(x,y,label='',color='y',s=100)
>      plt.xlabel("X")
>      plt.ylabel("Y")
>      plt.title("X vs Y")
>      plt.show() 
>   ```

#### Weighted Mean:

+ $Weightedd Mean  = ((Mean\ group \ 1)(N1) + (Mean\ group \ 2)(N1))/(N1+N2)$