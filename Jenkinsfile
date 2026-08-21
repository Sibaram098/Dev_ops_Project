stage('Deploy to Kubernetes') {
    steps {
        withCredentials([string(credentialsId: 'kubeconfig-credentials-id', variable: 'KUBECONFIG_B64')]) {
            sh '''
                echo "$KUBECONFIG_B64" | base64 -d > /tmp/kubeconfig
                sed -i "s|${DOCKER_IMAGE}:.*|${DOCKER_IMAGE}:${IMAGE_TAG}|g" k8s/deployment.yaml
                kubectl apply -f k8s/ --kubeconfig=/tmp/kubeconfig
                rm -f /tmp/kubeconfig
            '''
        }
    }
}
