
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
                bat 'docker build -t aws-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                    docker rm -f aws-app-container 2>nul || exit /b 0
                    docker run -d -p 5000:5000 --name aws-app-container aws-app
                '''
            }
        }
    }
}
