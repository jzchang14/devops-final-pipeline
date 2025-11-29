pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1444133402256085073/VMMWdkfphM1BLs4Wfj3udJQfEiwi-z3auX2QSaJ1a0VEhb1gFVLNRCdXxO4G5OZUpARm'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python venv & install dependencies') {
            steps {
                sh '''
                    set -eux

                    # Create virtual environment if it does not exist
                    if [ ! -d "$VENV_DIR" ]; then
                      python3 -m venv "$VENV_DIR"
                    fi

                    . "$VENV_DIR/bin/activate"

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    set -eux
                    . "$VENV_DIR/bin/activate"

                    echo "Running tests with pytest..."
                    pytest -v
                '''
            }
        }

        stage('Security scan (Bandit)') {
            steps {
                sh '''
                    set -eux
                    . "$VENV_DIR/bin/activate"

                    echo "Running security scan with bandit..."
                    bandit -r .
                '''
            }
        }

        stage('Notify Discord (success)) {
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
