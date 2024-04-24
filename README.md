## Getting Started  
  
These instructions will help you set up a virtual environment and run the project.  
  
### Prerequisites  
  
Before you proceed, make sure you have Python and `pip` installed on your system. You can verify the installation by running the following commands:  
  
```bash  
python --version  
pip --version    
```  
   
### Setting Up a Virtual Environment  
   
To create a virtual environment for this project, follow these steps:  
   
1. Install `virtualenv` if you haven't already:  
   
```bash  
pip install virtualenv  
```  
   
2. Navigate to the project directory and create a new virtual environment:  
   
```bash  
virtualenv venv  
```  
   
This will create a new directory called `venv` within the project folder. This directory contains the Python interpreter and the packages needed for the project.  
   
### Activating the Virtual Environment  
   
Before you start using the virtual environment, you need to activate it. To do so, run the following command:  
   
- On Windows:  
   
```bash  
venv\Scripts\activate  
```  
   
- On macOS and Linux:  
   
```bash  
source venv/bin/activate  
```  
   
After activating the virtual environment, your terminal should display a `(venv)` prefix.  
   
### Installing Dependencies  
   
With the virtual environment activated, install the project dependencies using the following command:  
   
```bash  
pip install -r requirements.txt  
```  
   
### Running the Project  
   
Now that you have set up and activated the virtual environment and installed the dependencies, you can run the project:  
   
```bash  
python codePortal.py  
```  
      
### Deactivating the Virtual Environment  
   
Once you're done working on the project, you can deactivate the virtual environment by running the following command:  
   
```bash  
deactivate  
```  
   
This will return you to the system's default Python interpreter.
