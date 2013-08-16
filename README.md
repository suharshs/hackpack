# hackpack
## Beautiful boilerplates to help start projects.

### To use this boilerplate:  
First, clone this repo.  
    ```$ git clone https://github.com/suharshs/hackpack.git```  

Then enter the hackpack.  
    ```$ cd hackpack```  

Finally run init_project.py to setup your project.  

```
$ python init_project.py --name your_project_name \  
                            --venv_base_dir venv_base_directory \  
                            --git_url your_git_url \  
                            --modules any extra modules you may want
```

### To start the server:
First, enter the virtualenv created by init_project.py.  
    ```$ workon your_project_name```  

You can now start the hello world server.  
    ```$ python server.py```


Requirements:  
1. Python  
2. Git  
3. Virtualenvwrapper  
