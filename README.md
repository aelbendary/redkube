# Running the redkube application in Minikube

This guide provides instructions for running a Flask application in Minikube.

# Prerequisites
* Minikube installed on your local machine
* Helm installed on your local machine
* Docker installed on your local machine
* The Flask application Docker image built and pushed to a Docker registry

#Steps

1. Start Minikube:
```    
      minikube start
```
2. Initialize Helm:
```    
      helm init
```
3. Clone the repository:
   Clone the repository containing the Flask application to your local machine.

4. Create a Helm chart for the Flask application:
   Create a Helm chart for the Flask application. The chart should specify the Docker image of the Flask application and any necessary configurations or parameters.

5. Install the Helm chart:
```
    helm install <chart-name> <path-to-chart-directory>
```
6. Access the application:
```
    minikube service <release-name>
```

# Conclusion

  This guide has provided the steps to run a Flask application in Minikube using Helm. The specific commands and names in this guide may vary based on the              specifics of your Flask application and your Minikube setup. 


