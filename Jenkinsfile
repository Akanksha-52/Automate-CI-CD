
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy to App Server') {
            steps {
                sh '''
                    scp -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=accept-new app.py requirements.txt Dockerfile ubuntu@52.90.236.141:/home/ubuntu/
                    ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=accept-new ubuntu@100.61.152.118 '
                        cd /home/ubuntu &&
                        docker build -t aws-app . &&
                        docker rm -f aws-app-container || true
                    '
                    ssh -i ~/.ssh/id_ed25519 ubuntu@100.61.152.118 'docker run -d --restart unless-stopped -p 5000:5000 --name aws-app-container aws-app'
                '''
            }
        }
    }
}
