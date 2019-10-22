# LSTM Proposed Approach UI

Welcome! This is the [LSTM Proposed Approach](https://link.springer.com/chapter/10.1007/978-3-030-26619-6_19) UI

![LSTM Proposed Approach Main Page](https://raw.githubusercontent.com/japoveda10/lstm_ui/master/lstm/IMAGE.png)

## What is it?

This is the User Interface of an [GenerativeLSTM](https://github.com/AdaptiveBProcess/GenerativeLSTM), an application that builds and uses generative models from event logs in XES format using LSTM neural networks.

## How is it built?

The UI is built using a Python framework called [Django](https://www.djangoproject.com/). This Python framework follows the **Model-Template-View** pattern. This project also uses [Chart.js](https://www.chartjs.org/).

## How can I run it?

1. Download this GitHub repository:

   ```
   $ git clone https://github.com/japoveda10/lstm_ui.git
   ```
   
2. Request the ```settings.py``` file to japoveda10 and then add it to the /lstm_ui/lstm/lstm/ directory
3. Install [Python](https://www.python.org/downloads/)
4. Create a **virtual environment** to manage the project's dependencies. If you are using **Windows**, follow the instructions available [here](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/). If you are using **macOS**, follow the instructions available [here](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html). 

**Important:** the virtual environment setup instructions for Windows and macOS were not written by us (we are linking you to an external information source).

4. Install **Django** using pip:

   ```
   $ pip install django
   ```

3. Execute the following commands to install the project's dependencies:

   ```
   $ pip install djangorestframework
   ```
   
   ```
   $ pip install psycopg2
   ```
   
   ```
   $ pip install pytz
   ```
   
   ```
   $ pip install sqlparse
   ```

4. Execute the following command:

   ```
   $ manage.py runserver
   ```

5. Open your web browser and go to:

   ```
   https://127.0.0.1:8000
   ```

## Questions and Suggestions

If you have questions or suggestions about this project, please contact [japoveda10](https://github.com/japoveda10)

## Author

By [japoveda10](https://github.com/japoveda10)
