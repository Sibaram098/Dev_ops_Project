node {
    def DOCKER_IMAGE = 'sibaram098/devops-microservice'
    def IMAGE_TAG = "${BUILD_NUMBER}"
    def DOCKER_HUB_CRED = 'dockerhub-credentials-id'
    def KUBE_CONFIG_CRED = 'kubeconfig-credentials-id'

    stage('Checkout Code') {
        checkout scm
    }

    stage('Build Docker Image') {
        sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ./app"
        sh "docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest"
    }

    stage('Push to Docker Hub') {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CRED}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
            sh '''
                docker login -u "$DOCKER_USER" -p "$DOCKER_PASS"
                docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                docker push ${DOCKER_IMAGE}:latest
            '''
        }
    }

    stage('Deploy to Kubernetes') {
        withCredentials([file(credentialsId: "${KUBE_CONFIG_CRED}", variable: 'KUBECONFIG')]) {
            sh '''
                sed -i "s|${DOCKER_IMAGE}:.*|${DOCKER_IMAGE}:${IMAGE_TAG}|g" k8s/deployment.yaml
                kubectl apply -f k8s/ --kubeconfig=$KUBECONFIG
            '''
        }
    }
}
