
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing Python dependencies'
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Flask tests'
                sh 'python3 -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f flask-app || true
                    docker run -d \
                      --name flask-app \
                      --restart unless-stopped \
                      -p 5000:5000 \
                      flask-app:latest
                '''
            }
        }
    }
}
