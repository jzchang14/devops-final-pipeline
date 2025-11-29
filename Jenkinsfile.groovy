// Jenkinsfile

pipeline {
    agent any

    environment {
        // Webex incoming webhook URL stored as a "Secret text" credential in Jenkins
        INCOMING_URL = credentials('webex-incoming-url')
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code from SCM..."
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                echo "Installing Python dependencies (pytest, bandit)..."
                sh '''
                    set -eux
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run unit tests') {
            steps {
                echo "Running pytest..."
                sh '''
                    set -eux
                    pytest
                '''
            }
        }

        stage('Run Bandit security scan') {
            steps {
                echo "Running Bandit security scan..."
                // -r . = recursively scan the current directory
                // -ll = only show issues with medium and high severity, keeps output manageable
                sh '''
                    set -eux
                    bandit -r . -ll
                '''
            }
        }
    }

    // Always send a Webex notification whether build passes or fails
    post {
        always {
            script {
                def result = currentBuild.currentResult  // "SUCCESS", "FAILURE", etc.

                echo "Sending Webex notification with build result: ${result}"

                // Simple one-line summary message to Webex space
                sh """
                    curl -X POST -H "Content-Type: application/json" \
                        -d '{ "markdown": "Jenkins job **${env.JOB_NAME}** build #${env.BUILD_NUMBER} finished with status **${result}**. Commit: `${env.GIT_COMMIT}`" }' \
                        $INCOMING_URL
                """
            }
        }
    }
}
