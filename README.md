# Introduction
"sbd-wml" stands for "**S**ilver **B**ullet on **D**eployment with **W**atson **M**achine **L**earning".
The aim is to deploy any python projects to IBM Cloud Pak for Data.

- Can be projects developed with Watson Studio in IBM Cloud Pak for Data
- Can be projects developed outside of Watson Studio
- It supports CPD 3.5/4.0/4.5
- It supports "batch job" well. "online" to be tested.
- It can be used to enable CI/CD.
- Support email notification when python scripts failed. 

Author: Jianbin Tang, jbtang@au1.ibm.com.

Feel free to "fork" it! 
If you like it, please "watch" and "star" the project. 

Also very much welcome your feedbacks and contributions! Thank you :)

License: Apache License 2.0


# Code Structure
- **code_example_to_be_deployed** : an example project code folder to be deployed.
- **deployment** : APIs to deploy any python projects to Watson Machine Learning deployment space.


# Usage

Set your working directory under **deployment**.

Please make sure you have latest **ibm-watson-machine-learning** package. I have it verified in 1.0.253 onwards.

```pip install ibm-watson-machine-learning --upgrade

```

## Step 1: Configure YAML file
Please make a copy of configuration_template.yaml and then modify the configuration accordingly.

## Step 2: Deploy!
Run below command to deploy your python code package:

```
python deploy_code_package.py --yaml_file [your_yaml_file] --test_run [True/False]
```

- If set "test_run" to be **True**: run the job immediately after deployment
- If set "test_run" to be **False**: only deploy the code package, but not run the job

Once successfully deployed, you will see below output(function_deployment_id will be different):

```
------------------------------------------------------------------------------------------------
Successfully finished deployment creation, deployment_uid='6f5fcc90-2931-4d46-b683-cc67aded2624'
------------------------------------------------------------------------------------------------


function_deployment_id = "6f5fcc90-2931-4d46-b683-cc67aded2624"
```

If you set "test_run" to be **True**, you will see below output in addition(job_id will be different):

```job_id: "da717590-10b7-45df-a12b-6e2f2345fc06" successfully submitted```

## Step 3: Run Job

Once the code package is successfully deployed, you can
- Either use CPD WebUI to schedule your job. More in: https://www.ibm.com/docs/en/cloud-paks/cp-data/4.5.x?topic=assets-creating-deployment-job
- Alternatively, you can run your job with below command, 
which is specifically useful when you want to use an external scheduler (eg. Control M): 

```python run_job.py --yamm_file [your_yaml_file]  --function_deployment_id=[function_deployment_id generated above]```

If successful, you will see below output (job_id will be different):

```job_id: "da717590-10b7-45df-a12b-6e2f2345fc06" successfully submitted```

### Additional Notes

- For data source connections/data assets created in Watson Studio, 
  you need to promote or replica those you needed in deployment space with exactly same configuration. 
  
- CPD3.5 needs complex workaround to connect data source connections in deployment space. 
Hence currently we recommend getting connection credentials inside your projects, eg from a local configuration file and so on.
This is not an issue for CPD4.x.
  
- For "model" deployment, we have 2 options here
  
    1) To develop a new API (Future work): 
       ```deploy_model --yaml_file [your_yaml_file]```
        
    2) Invoke your Model inside your own python projects, 
       then we can deploy with code package as well.
       
- "online" deployment will consume the CPU/Memory resources all the time, 
  while "batch job" only consume resource in a fractional time. 
Hence we only use it when it is very necessary. 
  Current code does provide "online" option, 
  but further verification/testing are needed.
