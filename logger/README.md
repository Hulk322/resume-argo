
----------------------------------------------------------------------------------------------------
								           Standard Logger For All SimplifyAI Tasks								  
----------------------------------------------------------------------------------------------

# How to Use: 
 
**Step 1:** Copy logger package in your directory
 
```javascript
 	    cp -r logger/ <DESTINATION PATH>
```
 
**Step 2:** Build Custom Logger
    
```python
 	from logger import standardLogger
 	test_logger = standardLogger().get_logger("My Test Logger")
 	test_logger.info("Hello World!")
```

get_logger has second parameter **kind_of_logger** to define the type of logger
We can choose anyone out of these 3 values for this parameter: 

*  logger.logger_config.CONSOLE_LOGGER

*  logger.logger_config.FILE_LOGGER

*  logger.logger_config.BOTH_CONSOLE_AND_FILE_LOGGER (this one is used by default)


**Step 3:** Import console logger for dependency libraries 
    
*If we wants to print the dependency libraries logs in our standard format then just copy these lines.*
    
**Import specific Logger (suppose we want logs on console):**
    
```python
 	from logger import standardLogger
	root = logging.getLogger()
	root.setLevel(logging.INFO)
	root.addHandler(standardLogger().get_console_handler())
```
 

# Sample Response: 
Response for the mentioned code snnipet:

	2020-06-09 15:57:34 INFO in 'My Test Logger' [<module>] at line 1: Hello World!
