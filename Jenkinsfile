
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aws-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker rm -f aws-app-container || true
                    docker run -d -p 5000:5000 --name aws-app-container aws-app
                '''
            }
        }
    }
}
