
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Flask Application'
                sh 'python3 -m compileall .'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Application'
                sh 'python3 -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image'
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Deploying Flask Application'
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
