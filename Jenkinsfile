pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1444133402256085073/VMMWdkfphM1BLs4Wfj3udJQfEiwi-z3auX2QSaJ1a0VEhb1gFVLNRCdXxO4G5OZUpARm'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    echo "Installing Python dependencies..."
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    echo "Running unit tests..."
                    python3 -m pytest -v
                '''
            }
        }

        stage('Notify Discord (success)') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                sh '''
                    echo "Sending success notification to Discord..."
                    curl -X POST \
                        -H "Content-Type: application/json" \
                        -d '{"content": "✅ Jenkins build for job devops-final-pipeline **SUCCEEDED**."}' \
                        "$DISCORD_WEBHOOK_URL"
                '''
            }
        }
    }

    post {
        failure {
            sh '''
                echo "Sending failure notification to Discord..."
                curl -X POST \
                    -H "Content-Type: application/json" \
                    -d '{"content": "❌ Jenkins build for job devops-final-pipeline **FAILED**. Check Jenkins for details."}' \
                    "$DISCORD_WEBHOOK_URL"
            '''
        }
    }
}
