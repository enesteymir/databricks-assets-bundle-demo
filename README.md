## Repository Structure

| Folder | File | Explanation
| ------ | ------ | ------ |
| job_definitions | wheel_job_definition.yml  : resource file that includes all settings for wheel_job.py and Cluster|
| job_definitions | notebook_job_definition.yml : resource file that includes all settings for noteboook_job.py and Cluster|
| job_sources/python_wheel_demo | wheel_job.py | python script that will be run by the wheel_job_definition.yml. |
| job_sources/notebook_demo | notebook_job.py | python script that will run by notebook_job_definition.yml. |
|  | databricks.yml | main bundle file that includes resources, artifacts, target environments etc  |
|  | poetry.lock | it is auto-generated file by poetry |
|  | delivery.yaml | it is used for CI/CD process and Service Principles will deploy the bundles to staging and prod |
|  | pyproject.toml | it is created by poetry but can be modified. The main package folder's name and the entry point to run is set here.  |


## How to Use Bundle Assets Locally

First, your Databricks CLI connection should be done. If you haven't done until now, check the [Configuring Databricks CLI](https://tracking.docs.zalando.net/how-to/databricks/databricks-cli/).

In your favourite text editor such as VS Code, clone the repository to your local:

After making changes to your branch, run the following command to check the structure of the bundle in your dev. You should receive "Validation OK!"" message.
> databricks bundle validate --target dev

If you have multiple connection profiles:
> databricks bundle validate --target dev --profile DEFAULT

If it is success, then you can deploy your bundle. This will build related bundle files in your user workspace folder and will create Jobs with your name on it.
> databricks bundle deploy --target dev


## Helpful Links

- Here is the Databricks documentation about What is Assets Bundle : https://docs.databricks.com/aws/en/dev-tools/bundles
- Here is the doc about configurations  : https://docs.databricks.com/aws/en/dev-tools/bundles/settings 
- Here is the doc about deployment modes : https://docs.databricks.com/aws/en/dev-tools/bundles/deployment-modes#development-mode 
- Here is another example from the Synapse Source Behaviour project's repository that is integrated with Assets Bundle, please check README also : https://github.bus.zalan.do/t-rex/source-behavioral-data 
- Here is the example Bundle Assets template repo provided by the Team Wrangler  : https://github.bus.zalan.do/wrangler/databricks_asset_bundle_example 

## How to Set Up a Repo from scratch integrated with Bundle Assets ?

There are multiple ways to do it, you can use the documentation links above. Here is the fast and manual way:

- Create a new blank repository
- Create job_sources and job_definitions folders. Copy these config files to your repository : databricks.yml , pyproject.toml. 
- Add your job scripts and related cluster definition files. Modify all the config files based on your new structure.
- Connect to your repository from the terminal and install poetry. It will create **poetry.lock** file automatically.

```sh
    brew install poetry
    poetry install
```

- Finally validate your bundle.
> databricks bundle validate --target dev

- If it is succeded, you are ready to go. Push your changes to the remote repo.