# Live-Score-script


### _This script uses the URL of Cricbuzz to display the current score of the match with the Team Name. The URL is to be provided by the User. Also the script refreshes itself after a specific amount of time which is to be specified by the User when asked._

### Tools required:
```  
  Python3
  BeautifulSoup
  requests
```
### For linux users:
###   If **_\#Python3, \#BeatifulSoup_** and **_\#requests_** is not installed
   **Use:**
```
$ sudo apt-get install python3
$ sudo apt-get install python3-bs4
$ sudo apt-get install python3-requests
```
#### To use the script:
  1. Download the bash and python script
  
  2. Save them in the same folder
  
  3. Open terminal and type
  ```
  bash cricket.sh
  ```
  4. Or you can make the bash file executable by using command:
    ```
  chmod +x cricket.sh
    ```
     
    * **_Note_**:If the bash script is made executable, It can be run by double-clicking it and choosing **Run in Terminal.**
  
  5. Then put the time-interval for which you want to refresh the script (Just input an
    integer & time will be in seconds)
  
  6. Later input the URL of Page on Cricbuzz where scorecard is displayed and Enter.
  
#### You will see the score in format:
  For eg.
  ```
    India Innings
     Total     123    (1  wkts, 25 Ov)
  ```   
  which will be refreshed after every **n** seconds ( **_n = time input by User_** )  
    
    
