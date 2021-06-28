  
  
# File Operation
  
  
## File
  
  
+ FIle is collection of related information.
+ Is used to store the data parmanently in file.
+ Can perform following list of operation:
  
  1. Open file
  2. Read or write
  3. Append
  4. Close
  
### 1. Opening a file
  
  
+ python has built-in function **open()** to open a file object
+ It return a file object.
+ >```python
  > #syntax
  >fileObjdect = open(fileName[,accessmode][,buffering]) 
  > ```
  
|Function|Dexcription|
|:---|:---|
|<img src="https://latex.codecogs.com/gif.latex?open()"/>|opens a file and return an object|
|<img src="https://latex.codecogs.com/gif.latex?close()"/>|used to close the file|
  
#### Different Modes
  
  
|Modes|Dexcription|
|:---|:---|
|<img src="https://latex.codecogs.com/gif.latex?r"/>|Open for reading only|
|<img src="https://latex.codecogs.com/gif.latex?rb"/>|reading in binary mode|
|<img src="https://latex.codecogs.com/gif.latex?b"/>|open in binary mode|
|<img src="https://latex.codecogs.com/gif.latex?r+"/>|open for reading and writing as well|
|<img src="https://latex.codecogs.com/gif.latex?rb+"/>|reading and writing in binary mode|
|<img src="https://latex.codecogs.com/gif.latex?W"/>|opens a file for writing only|
|<img src="https://latex.codecogs.com/gif.latex?a"/>|opens a file for appending and reading|
|<img src="https://latex.codecogs.com/gif.latex?t"/>|open in text mode(default)|
|<img src="https://latex.codecogs.com/gif.latex?+"/>|open a file for updating (reading and writing)|
  
#### File object attribute
  
  
+ After opening a file object has following attribute
  
|Attribute|Description|
|:---|:----|
|Myfile<img src="https://latex.codecogs.com/gif.latex?.closed"/>|Returns true if file is closed|
|Myfile<img src="https://latex.codecogs.com/gif.latex?.mode"/>|Returns access Mode|
|Myfile<img src="https://latex.codecogs.com/gif.latex?.name"/>|Returns name of the file.|
  
#### File object Methods
  
  
|Functions|Description|Syntax|
|:---|:---|:---|
|<img src="https://latex.codecogs.com/gif.latex?read()"/>|It reads data depands up on size of character read(size). If size parameter read is not specified,it reads complete file.|FileObject.read([count])|
|<img src="https://latex.codecogs.com/gif.latex?readline()"/>|To read individual line of a file.|FileObject.readline()|
|<img src="https://latex.codecogs.com/gif.latex?tell()"/>|The tell() method tells you the current cusor position within a file.|FileObject.tell()|
|<img src="https://latex.codecogs.com/gif.latex?seek()"/>|This method change the cursor position in the file.|seek(Offset[,]) <br>seek(0,0)|
  