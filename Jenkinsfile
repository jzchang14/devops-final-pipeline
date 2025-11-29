pipeline {
    agent any

    environment {
        // ❗ Replace this with your actual Discord webhook URL
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1444133402256085073/VMMWdkfphM1BLs4Wfj3udJQfEiwi-z3auX2QSaJ1a0VEhb1gFVLNRCdXxO4G5OZUpARm'
    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins will automatically check out from GitHub,
                // but this makes it explicit for clarity
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    echo "Installing Python dependencies..."
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    echo "Running tests with pytest..."
                    pytest
                '''
            }
        }

        stage('Notify Discord (success)') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                script {
                    def msg = "✅ Jenkins build #${env.BUILD_NUMBER} for job '${env.JOB_NAME}' **SUCCEEDED**."
                    sh """
                        curl -X POST -H 'Content-Type: application/json' \
                          -d '{\"content\": \"${msg}\"}' \
                          ${DISCORD_WEBHOOK_URL}
                    """
                }
            }
        }
    }

    post {
        failure {
            script {
                def msg = "❌ Jenkins build #${env.BUILD_NUMBER} for job '${env.JOB_NAME}' **FAILED**. Check Jenkins for details."
                sh """
                    curl -X POST -H 'Content-Type: application/json' \
                      -d '{\"content\": \"${msg}\"}' \
                      ${DISCORD_WEBHOOK_URL}
                """
            }
        }
    }
}
