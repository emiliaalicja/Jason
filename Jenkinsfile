pipeline {
    agent any

    triggers {
        cron('H/2 * * * *')  // uruchamiane co 2 minuty
    }

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello world!', description: 'Message to be displayed')
    }

    stages {
        stage('Say Message') {
            steps {
                echo "Message: ${params.MESSAGE}"
            }
        }
    }
}