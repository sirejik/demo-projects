# argparse-hello-world
Here is an example of how to parse arguments in the python script and configure logging.

## Run project.
To get help on the script, run the following command:
```
python main.py --help
```
You can specify only required arguments:
```
python main.py --required-argument 1
```
Or specify all required and optional arguments:
```
python main.py --required-argument 1 --optional-argument hello
```
## Logging.
All information will be saved in the log file:
```
debug.log
```
Also, all info and error logs will be shown on the output.
