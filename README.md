# python microservices
#  docker command
docker build -t webapp:1.0 . <br />
docker run -d -p 80:5051 --name web webapp:1.0 <br />
minikube ip <br />
docker rm -f web <br />
# docker-compose command
docker-compose build <br />
docker-compose up -d <br />
minikube ip <br />
docker-compose down <br />

# kubernetes command
kubectl apply -f deployment.yml <br />
kubectl get po <br />
kubectl apply -f service.yml <br />
kubectl get po,svc <br />
minikube ip:(port from above) <br />
kubectl delete -f . <br />

# helm commands
helm create webapp <br />
helm template webapp <br />
helm install web webapp/ <br />
helm list <br />
kubectl get po,svc <br />
minikube ip:(port from above) <br />
helm uninstall web <br />


